# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2023-05-09 15:30:10
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Operation system methods.
"""


from __future__ import annotations
from typing import Any, List, Union, Literal, Optional, NoReturn, overload
from io import TextIOBase, BufferedIOBase
from json import JSONDecodeError
from os import (
    walk as os_walk,
    listdir as os_listdir,
    makedirs as os_makedirs,
    renames as os_renames,
    remove as os_remove
)
from os.path import (
    abspath as os_abspath,
    join as os_join,
    isfile as os_isfile,
    isdir as os_isdir,
    basename as os_basename,
    dirname as os_dirname,
    exists as os_exists,
    getsize as os_getsize,
    getctime as os_getctime,
    getmtime as os_getmtime,
    getatime as os_getatime,
    split as os_split,
    splitext as os_splitext,
    splitdrive as os_splitdrive
)
from shutil import copy
from hashlib import md5 as hashlib_md5
from tempfile import TemporaryFile, TemporaryDirectory
from docx import Document as docx_document
from docx.document import Document
from docx.text.paragraph import Paragraph
from docx.table import Table
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from lxml.etree import ElementChildIterator
from pdfplumber import open as pdfplumber_open

from .rregex import search, sub
from .rsystem import throw, dos_command
from .rtext import to_json


__all__ = (
    "get_md5",
    "create_folder",
    "find_relpath",
    "get_file_str",
    "get_file_bytes",
    "RFile",
    "RFolder",
    "RTempFile",
    "RTempFolder",
    "doc_to_docx",
    "extract_docx_content",
    "extract_pdf_content",
    "extract_file_content"
)


FileStr = Union[str, TextIOBase]
FileBytes = Union[bytes, str, BufferedIOBase]
File = Union[FileStr, FileBytes]


def get_md5(file: Union[str, bytes]) -> str:
    """
    Get file MD5.

    Parameters
    ----------
    file : File path or file bytes.

    Returns
    -------
    File MD5.
    """

    # Get bytes.

    ## Path.
    if file.__class__ == str:
        rfile = RFile(file)
        file_bytes = rfile.bytes

    ## Bytes.
    elif file.__class__ == bytes:
        file_bytes = file

    # Calculate.
    hash = hashlib_md5(file_bytes)
    md5 = hash.hexdigest()

    return md5


def create_folder(*paths: str, report: bool = False) -> None:
    """
    Create folders.

    Parameters
    ----------
    paths : Folder paths.
    report : Whether report the creation process.
    """

    # Create.
    for path in paths:
        rfolder = RFolder(path)
        rfolder.create(report)


def find_relpath(abspath: str, relpath: str) -> str:
    """
    Based absolute path and symbol `.` of relative path, find a new absolute path.

    Parameters
    ----------
    abspath : Original absolute path.
    relpath : relative path.

    Returns
    -------
    New absolute path.

    Examples
    --------
    >>> old_abspath = os.getcwd()
    >>> relpath = '..\Folder4\File.txt'
    >>> new_abspath = convert_relpath(old_abspath, relpath)
    >>> old_abspath
    C:\Folder1\Folder2\Folder3
    >>> new_abspath
    C:\Folder1\Folder4\File.txt
    """

    # Get parameter.
    level = 0
    for char in relpath:
        if char == ".":
            level += 1
        else:
            break
    strip_n = 0
    for char in relpath[level:]:
        if char in ("/", "\\"):
            strip_n += 1
        else:
            break

    # Convert.
    folder_path = abspath
    for _ in range(level):
        folder_path, _ = os_split(folder_path)
    relpath = relpath[level + strip_n:]
    path = os_join(folder_path, relpath)

    return path


def get_file_str(file: FileStr) -> str:
    """
    Get file string data.

    Parameters
    ----------
    file : File source.
        - `'str' and path` : Return this string data.
        - `'str' and not path` : As a file path read string data.
        - `TextIOBase` : Read string data.

    Returns
    -------
    File string data.
    """

    # Path or string.
    if file.__class__ == str:
        exist = os_exists(file)

        # Path.
        if exist:
            rfile = RFile(file)
            file_str = rfile.str

        # String.
        else:
            file_str = file

    # IO.
    elif isinstance(file, TextIOBase):
        file_str = file.read()

    # Throw exception.
    else:
        throw(TypeError, file)

    return file_str


@overload
def get_file_bytes(file: FileBytes) -> bytes: ...

@overload
def get_file_bytes(file: Any) -> NoReturn: ...

def get_file_bytes(file: FileBytes) -> bytes:
    """
    Get file bytes data.

    Parameters
    ----------
    file : File source.
        - `bytes` : Return this bytes data.
        - `str` : As a file path read bytes data.
        - `BufferedIOBase` : Read bytes data.

    Returns
    -------
    File bytes data.
    """

    # Bytes.
    if file.__class__ == bytes:
        file_bytes = file

    # Path.
    elif file.__class__ == str:
        rfile = RFile(file)
        file_bytes = rfile.bytes

    # IO.
    elif isinstance(file, BufferedIOBase):
        file_bytes = file.read()

    # Throw exception.
    else:
        throw(TypeError, file)

    return file_bytes


class RFile(object):
    """
    Rey's `file` type.
    """


    def __init__(
        self,
        path: str
    ) -> None:
        """
        Build `file` instance.

        Parameters
        ----------
        path : File path.
        """

        # Set attribute.
        self.path = os_abspath(path)


    @overload
    def read(
        self,
        type_: Literal["bytes"] = "bytes"
    ) -> bytes: ...

    @overload
    def read(
        self,
        type_: Literal["str"] = "bytes"
    ) -> str: ...

    def read(
        self,
        type_: Literal["str", "bytes"] = "bytes"
    ) -> Union[bytes, str]:
        """
        Read file data.

        Parameters
        ----------
        type_ : File data type.
            - `Literal['bytes']` : Return file bytes data.
            - `Literal['str']` : Return file string data.

        Returns
        -------
        File data.
        """

        # Handle parameter.
        if type_ == "bytes":
            mode = "rb"
            encoding = None
        elif type_ == "str":
            mode = "r"
            encoding="utf-8"

        # Read.
        with open(self.path, mode, encoding=encoding) as file:
            content = file.read()

        return content


    def write(
        self,
        data: Optional[Any] = "",
        append: bool = False
    ) -> None:
        """
        Write file data.

        Parameters
        ----------
        data : Write data.
            - `str` : File text.
            - `bytes` : File bytes data.
            - `Any` : To JSON format or string.

        append : Whether append data, otherwise overwrite data.
        """

        # Handle parameter.

        ## Write mode.
        if append:
            mode = "a"
        else:
            mode = "w"
        if data.__class__ == bytes:
            mode += "b"

        ## Convert data to string.
        if data.__class__ not in (str, bytes):
            try:
                data = to_json(data)
            except (JSONDecodeError, TypeError):
                data = str(data)

        # Write.
        with open(self.path, mode) as file:
            file.write(data)


    def copy(
        self,
        path: str
    ) -> None:
        """
        Copy file to path.

        Parameters
        ----------
        path : Copy path.
        """

        # Copy.
        copy(
            self.path,
            path
        )


    def move(
        self,
        path: str
    ) -> None:
        """
        Move file to path.

        Parameters
        ----------
        path : Move path.
        """

        # Move.
        os_renames(
            self.path,
            path
        )


    def remove(
        self
    ) -> None:
        """
        Remove file.
        """

        # Copy.
        try:
            os_remove(self.path)

        # Read only.
        except PermissionError:
            command = f"attrib -r \"{self.path}\""
            dos_command(command)
            os_remove(self.path)


    @property
    def str(self) -> str:
        """
        Read content as a string.

        Returns
        -------
        File string content.
        """

        # Read.
        file_str = self.read("str")

        return file_str


    @property
    def bytes(self) -> bytes:
        """
        Read content in byte form.

        Returns
        -------
        File bytes content.
        """

        # Read.
        file_bytes = self.read("bytes")

        return file_bytes


    @property
    def name_suffix(self) -> str:
        """
        Return file name with suffix.

        Returns
        -------
        File name with suffix.
        """

        # Get.
        file_name_suffix = os_basename(self.path)

        return file_name_suffix


    @property
    def name(self) -> str:
        """
        Return file name not with suffix.

        Returns
        -------
        File name not with suffix.
        """

        # Get.
        file_name, _ = os_splitext(self.name_suffix)

        return file_name


    @property
    def suffix(self) -> str:
        """
        Return file suffix.

        Returns
        -------
        File suffix.
        """

        # Get.
        _, file_suffix = os_splitext(self.path)

        return file_suffix


    @property
    def dir(self) -> str:
        """
        Return file directory.

        Returns
        -------
        File directory.
        """

        # Get.
        file_dir = os_dirname(self.path)

        return file_dir


    @property
    def drive(self) -> str:
        """
        Return file drive letter.

        Returns
        -------
        File drive letter.
        """

        # Get.
        file_drive, _ = os_splitdrive(self.path)

        return file_drive


    @property
    def size(self) -> int:
        """
        Return file byte size.

        Returns
        -------
        File byte size.
        """

        # Get.
        file_size = os_getsize(self.path)

        return file_size


    @property
    def ctime(self) -> float:
        """
        Return file create timestamp.

        Returns
        -------
        File create timestamp.
        """

        # Get.
        file_ctime = os_getctime(self.path)

        return file_ctime


    @property
    def mtime(self) -> float:
        """
        Return file modify timestamp.

        Returns
        -------
        File modify timestamp.
        """

        # Get.
        file_mtime = os_getmtime(self.path)

        return file_mtime


    @property
    def atime(self) -> float:
        """
        Return file access timestamp.

        Returns
        -------
        File access timestamp.
        """

        # Get.
        file_atime = os_getatime(self.path)

        return file_atime


    @property
    def md5(self) -> float:
        """
        Return file MD5 value.

        Returns
        -------
        File MD5 value
        """

        # Get.
        file_md5 = get_md5(self.path)

        return file_md5


    def __bool__(self) -> bool:
        """
        Judge if exist.

        Returns
        -------
        Judge result.
        """

        # Judge.
        file_exist = os_isfile(self.path)

        return file_exist


    def __len__(self) -> int:
        """
        Return file byte size.

        Returns
        -------
        File byte size.
        """

        # Get.
        file_size = self.size

        return file_size


    def __str__(self) -> str:
        """
        Read content as a string.

        Returns
        -------
        File string content.
        """

        # Read.
        file_text = self.str

        return file_text


    def __bytes__(self) -> bytes:
        """
        Read content in byte form.

        Returns
        -------
        File bytes content.
        """

        # Read.
        file_bytes = self.bytes

        return file_bytes


    def __contains__(
        self,
        value: Union[str, bytes]
    ) -> bool:
        """
        Judge if file text contain value.

        Parameters
        ----------
        value : Judge value.

        Returns
        -------
        Judge result.
        """

        # Get parameter.
        if value.__class__ == str:
            content = self.str
        elif value.__class__ == bytes:
            content = self.bytes
        else:
            throw(TypeError, value)

        # Judge.
        judge = value in content

        return judge


    __call__ = write


class RFolder(object):
    """
    Rey's `folder` type.
    """


    def __init__(
        self,
        path: Optional[str] = None
    ) -> None:
        """
        Build `folder` instance.

        Parameters
        ----------
        path : Folder path.
            - `None` : Work folder path.
            - `str` : Use this folder path.
        """

        # Set attribute.
        if path is None:
            path = ""
        self.path = os_abspath(path)


    def paths(
        self,
        target: Literal["all", "file", "folder"] = "all",
        recursion: bool = False
    ) -> List:
        """
        Get the path of files and folders in the folder path.

        Parameters
        ----------
        target : Target data.
            - `Literal['all']` : Return file and folder path.
            - `Literal['file']` : Return file path.
            - `Literal['folder']` : Return folder path.

        recursion : Is recursion directory.

        Returns
        -------
        String is path.
        """

        # Get paths.
        paths = []

        ## Recursive.
        if recursion:
            obj_walk = os_walk(self.path)
            if target == "all":
                targets_path = [
                    os_join(path, file_name)
                    for path, folders_name, files_name in obj_walk
                    for file_name in files_name + folders_name
                ]
                paths.extend(targets_path)
            elif target == "file":
                targets_path = [
                    os_join(path, file_name)
                    for path, _, files_name in obj_walk
                    for file_name in files_name
                ]
                paths.extend(targets_path)
            elif target in ("all", "folder"):
                targets_path = [
                    os_join(path, folder_name)
                    for path, folders_name, _ in obj_walk
                    for folder_name in folders_name
                ]
                paths.extend(targets_path)

        ## Non recursive.
        else:
            names = os_listdir(self.path)
            if target == "all":
                for name in names:
                    target_path = os_join(self.path, name)
                    paths.append(target_path)
            elif target == "file":
                for name in names:
                    target_path = os_join(self.path, name)
                    is_file = os_isfile(target_path)
                    if is_file:
                        paths.append(target_path)
            elif target == "folder":
                for name in names:
                    target_path = os_join(self.path, name)
                    is_dir = os_isdir(target_path)
                    if is_dir:
                        paths.append(target_path)

        return paths


    @overload
    def search(
        self,
        pattern: str,
        recursion: bool = False,
        all_ : Literal[False] = False
    ) -> Optional[str]: ...

    @overload
    def search(
        self,
        pattern: str,
        recursion: bool = False,
        all_ : Literal[True] = False
    ) -> List[str]: ...

    def search(
        self,
        pattern: str,
        recursion: bool = False,
        all_ : bool = False
    ) -> Optional[str]:
        """
        Search file by name.

        Parameters
        ----------
        pattern : Match file name pattern.
        recursion : Is recursion directory.
        all_ : Whether return all match file path, otherwise return first match file path.

        Returns
        -------
        Match file path or null.
        """

        # Get paths.
        file_paths = self.paths("file", recursion)

        # All.
        if all_:
            match_paths = []
            for path in file_paths:
                file_name = os_basename(path)
                result = search(pattern, file_name)
                if result is not None:
                    match_paths.append(path)
            return match_paths

        # First.
        else:
            for path in file_paths:
                file_name = os_basename(path)
                result = search(pattern, file_name)
                if result is not None:
                    return path


    def create(
        self,
        report: bool = False
    ) -> None:
        """
        Create folders.

        Parameters
        ----------
        report : Whether report the creation process.
        """

        # Exist.
        exist = os_exists(self.path)
        if exist:
            text = "Folder already exists    | %s" % self.path

        # Not exist.
        else:
            os_makedirs(self.path)
            text = "Folder creation complete | %s" % self.path

        # Report.
        if report:
            print(text)


    def move(
        self,
        path: str
    ) -> None:
        """
        Move folder to path.

        Parameters
        ----------
        path : Move path.
        """

        # Move.
        os_renames(
            self.path,
            path
        )


    @property
    def name(self) -> str:
        """
        Return folder name.

        Returns
        -------
        Folder name.
        """

        # Get.
        folder_name = os_basename(self.path)

        return folder_name


    @property
    def dir(self) -> str:
        """
        Return folder directory.

        Returns
        -------
        Folder directory.
        """

        # Get.
        folder_dir = os_dirname(self.path)

        return folder_dir


    @property
    def drive(self) -> str:
        """
        Return folder drive letter.

        Returns
        -------
        Folder drive letter.
        """

        # Get.
        folder_drive, _ = os_splitdrive(self.path)

        return folder_drive


    @property
    def size(self) -> int:
        """
        Return folder byte size, include all files in it.

        Returns
        -------
        Folder byte size.
        """

        # Get.
        file_paths = self.paths("file", True)
        file_sizes = [
            os_getsize(path)
            for path in file_paths
        ]
        folder_size = sum(file_sizes)

        return folder_size


    @property
    def ctime(self) -> float:
        """
        Return file create timestamp.

        Returns
        -------
        File create timestamp.
        """

        # Get.
        folder_ctime = os_getctime(self.path)

        return folder_ctime


    @property
    def mtime(self) -> float:
        """
        Return file modify timestamp.

        Returns
        -------
        File modify timestamp.
        """

        # Get.
        folder_mtime = os_getmtime(self.path)

        return folder_mtime


    @property
    def atime(self) -> float:
        """
        Return file access timestamp.

        Returns
        -------
        File access timestamp.
        """

        # Get.
        folder_atime = os_getatime(self.path)

        return folder_atime


    def __bool__(self) -> bool:
        """
        Judge if exist.

        Returns
        -------
        Judge result.
        """

        # Judge.
        folder_exist = os_isdir(self.path)

        return folder_exist


    def __len__(self) -> int:
        """
        Return folder byte size, include all files in it.

        Returns
        -------
        Folder byte size.
        """

        # Get.
        folder_size = self.size

        return folder_size


    def __contains__(self, pattern: str) -> bool:
        """
        Search file by name, recursion directory.

        Parameters
        ----------
        pattern : Match file name pattern.

        Returns
        -------
        Judge result.
        """

        # Judge.
        result = self.search(pattern, True)
        judge = result is not None

        return judge


    __call__ = paths


class RTempFile(object):
    """
    Rey's `temporary file` type.
    """


    def __init__(
        self,
        dir_: Optional[str] = None,
        suffix: Optional[str] = None,
        type_: Literal["str", "bytes"] = "bytes"
    ) -> None:
        """
        Build `temporary file` instance.

        Parameters
        ----------
        dir_ : Directory path.
        suffix : File suffix.
        type_ : File data type.
        """

        # Get parameter.
        if type_ == "bytes":
            mode = "w+b"
        elif type_ == "str":
            mode = "w+"
        else:
            throw(ValueError, type_)

        # Set attribute.
        self.file = TemporaryFile(
            mode,
            suffix=suffix,
            dir=dir_
        )
        self.path = self.file.name


    def read(self) -> Union[bytes, str]:
        """
        Read file data.

        Returns
        -------
        File data.
        """

        # Read.
        self.file.seek(0)
        content = self.file.read()

        return content


    def write(
        self,
        data: Union[str, bytes]
    ) -> None:
        """
        Write file data.

        Parameters
        ----------
        data : Write data.
        """

        # Write.
        self.file.write(data)
        self.file.seek(0)


    @property
    def name_suffix(self) -> str:
        """
        Return file name with suffix.

        Returns
        -------
        File name with suffix.
        """

        # Get.
        file_name_suffix = os_basename(self.path)

        return file_name_suffix


    @property
    def name(self) -> str:
        """
        Return file name not with suffix.

        Returns
        -------
        File name not with suffix.
        """

        # Get.
        file_name, _ = os_splitext(self.name_suffix)

        return file_name


    @property
    def suffix(self) -> str:
        """
        Return file suffix.

        Returns
        -------
        File suffix.
        """

        # Get.
        _, file_suffix = os_splitext(self.path)

        return file_suffix


    @property
    def dir(self) -> str:
        """
        Return file directory.

        Returns
        -------
        File directory.
        """

        # Get.
        file_dir = os_dirname(self.path)

        return file_dir


    @property
    def drive(self) -> str:
        """
        Return file drive letter.

        Returns
        -------
        File drive letter.
        """

        # Get.
        file_drive, _ = os_splitdrive(self.path)

        return file_drive


    @property
    def size(self) -> int:
        """
        Return file byte size.

        Returns
        -------
        File byte size.
        """

        # Get.
        file_size = os_getsize(self.path)

        return file_size


    @property
    def ctime(self) -> float:
        """
        Return file create timestamp.

        Returns
        -------
        File create timestamp.
        """

        # Get.
        file_ctime = os_getctime(self.path)

        return file_ctime


    @property
    def mtime(self) -> float:
        """
        Return file modify timestamp.

        Returns
        -------
        File modify timestamp.
        """

        # Get.
        file_mtime = os_getmtime(self.path)

        return file_mtime


    @property
    def atime(self) -> float:
        """
        Return file access timestamp.

        Returns
        -------
        File access timestamp.
        """

        # Get.
        file_atime = os_getatime(self.path)

        return file_atime


    @property
    def md5(self) -> float:
        """
        Return file MD5 value.

        Returns
        -------
        File MD5 value
        """

        # Get.
        file_md5 = get_md5(self.path)

        return file_md5


    def __len__(self) -> int:
        """
        Return file byte size.

        Returns
        -------
        File byte size.
        """

        # Get.
        file_size = self.size

        return file_size


    def __contains__(
        self,
        value: Union[str, bytes]
    ) -> bool:
        """
        Judge if file text contain value.

        Parameters
        ----------
        value : Judge value.

        Returns
        -------
        Judge result.
        """

        # Get parameter.
        content = self.read()

        # Judge.
        judge = value in content

        return judge


    def __del__(self) -> None:
        """
        Close temporary file.
        """

        # Close.
        self.file.close()


    __call__ = write


class RTempFolder(object):
    """
    Rey's `temporary folder` type.
    """


    def __init__(
        self,
        dir_: Optional[str] = None
    ) -> None:
        """
        Build `temporary folder` instance.

        Parameters
        ----------
        dir_ : Directory path.
        """

        # Set attribute.
        self.folder = TemporaryDirectory(dir=dir_)
        self.path = os_abspath(self.folder.name)


    def paths(
        self,
        target: Literal["all", "file", "folder"] = "all",
        recursion: bool = False
    ) -> List:
        """
        Get the path of files and folders in the folder path.

        Parameters
        ----------
        target : Target data.
            - `Literal['all']` : Return file and folder path.
            - `Literal['file']` : Return file path.
            - `Literal['folder']` : Return folder path.

        recursion : Is recursion directory.

        Returns
        -------
        String is path.
        """

        # Get paths.
        paths = []

        ## Recursive.
        if recursion:
            obj_walk = os_walk(self.path)
            if target == "all":
                targets_path = [
                    os_join(path, file_name)
                    for path, folders_name, files_name in obj_walk
                    for file_name in files_name + folders_name
                ]
                paths.extend(targets_path)
            elif target == "file":
                targets_path = [
                    os_join(path, file_name)
                    for path, _, files_name in obj_walk
                    for file_name in files_name
                ]
                paths.extend(targets_path)
            elif target in ("all", "folder"):
                targets_path = [
                    os_join(path, folder_name)
                    for path, folders_name, _ in obj_walk
                    for folder_name in folders_name
                ]
                paths.extend(targets_path)

        ## Non recursive.
        else:
            names = os_listdir(self.path)
            if target == "all":
                for name in names:
                    target_path = os_join(self.path, name)
                    paths.append(target_path)
            elif target == "file":
                for name in names:
                    target_path = os_join(self.path, name)
                    is_file = os_isfile(target_path)
                    if is_file:
                        paths.append(target_path)
            elif target == "folder":
                for name in names:
                    target_path = os_join(self.path, name)
                    is_dir = os_isdir(target_path)
                    if is_dir:
                        paths.append(target_path)

        return paths


    @overload
    def search(
        self,
        pattern: str,
        recursion: bool = False,
        all_ : Literal[False] = False
    ) -> Optional[str]: ...

    @overload
    def search(
        self,
        pattern: str,
        recursion: bool = False,
        all_ : Literal[True] = False
    ) -> List[str]: ...

    def search(
        self,
        pattern: str,
        recursion: bool = False,
        all_ : bool = False
    ) -> Optional[str]:
        """
        Search file by name.

        Parameters
        ----------
        pattern : Match file name pattern.
        recursion : Is recursion directory.
        all_ : Whether return all match file path, otherwise return first match file path.

        Returns
        -------
        Match file path or null.
        """

        # Get paths.
        file_paths = self.paths("file", recursion)

        # All.
        if all_:
            match_paths = []
            for path in file_paths:
                file_name = os_basename(path)
                result = search(pattern, file_name)
                if result is not None:
                    match_paths.append(path)
            return match_paths

        # First.
        else:
            for path in file_paths:
                file_name = os_basename(path)
                result = search(pattern, file_name)
                if result is not None:
                    return path


    @property
    def name(self) -> str:
        """
        Return folder name.

        Returns
        -------
        Folder name.
        """

        # Get.
        folder_name = os_basename(self.path)

        return folder_name


    @property
    def dir(self) -> str:
        """
        Return folder directory.

        Returns
        -------
        Folder directory.
        """

        # Get.
        folder_dir = os_dirname(self.path)

        return folder_dir


    @property
    def drive(self) -> str:
        """
        Return folder drive letter.

        Returns
        -------
        Folder drive letter.
        """

        # Get.
        folder_drive, _ = os_splitdrive(self.path)

        return folder_drive


    @property
    def size(self) -> int:
        """
        Return folder byte size, include all files in it.

        Returns
        -------
        Folder byte size.
        """

        # Get.
        file_paths = self.paths("file", True)
        file_sizes = [
            os_getsize(path)
            for path in file_paths
        ]
        folder_size = sum(file_sizes)

        return folder_size


    @property
    def ctime(self) -> float:
        """
        Return file create timestamp.

        Returns
        -------
        File create timestamp.
        """

        # Get.
        folder_ctime = os_getctime(self.path)

        return folder_ctime


    @property
    def mtime(self) -> float:
        """
        Return file modify timestamp.

        Returns
        -------
        File modify timestamp.
        """

        # Get.
        folder_mtime = os_getmtime(self.path)

        return folder_mtime


    @property
    def atime(self) -> float:
        """
        Return file access timestamp.

        Returns
        -------
        File access timestamp.
        """

        # Get.
        folder_atime = os_getatime(self.path)

        return folder_atime


    def __bool__(self) -> bool:
        """
        Judge if exist.

        Returns
        -------
        Judge result.
        """

        # Judge.
        folder_exist = os_isdir(self.path)

        return folder_exist


    def __len__(self) -> int:
        """
        Return folder byte size, include all files in it.

        Returns
        -------
        Folder byte size.
        """

        # Get.
        folder_size = self.size

        return folder_size


    def __contains__(self, pattern: str) -> bool:
        """
        Search file by name, recursion directory.

        Parameters
        ----------
        pattern : Match file name pattern.

        Returns
        -------
        Judge result.
        """

        # Judge.
        result = self.search(pattern, True)
        judge = result is not None

        return judge


    def __del__(self) -> None:
        """
        Close temporary folder.
        """

        # Close.
        self.folder.cleanup()


    __call__ = paths


def doc_to_docx(
    path: str,
    save_path: Optional[str] = None
) -> str:
    """
    Convert `DOC` file to `DOCX` file.

    Parameters
    ----------
    path : DOC file path.
    save_path : DOCX sve file path.
        - `None` : DOC file Directory.

    Returns
    -------
    DOCX file path.
    """


    from win32com.client import Dispatch, CDispatch


    # Handle parameter.
    if save_path is None:
        pattern = ".[dD][oO][cC]"
        save_path = sub(
            pattern,
            path.replace("\\", "/"),
            ".docx"
        )

    # Convert.
    cdispatch = Dispatch('Word.Application')
    document: CDispatch = cdispatch.Documents.Open(path)
    document.SaveAs(save_path, 16)
    document.Close()

    return save_path


def extract_docx_content(path: str) -> str:
    """
    Extract content from `DOCX` file.

    Parameters
    ----------
    path : File path.

    returns
    -------
    Content.
    """

    # Extract.
    document: Document = docx_document(path)
    childs_iter: ElementChildIterator = document.element.body.iterchildren()
    contents = []
    for child in childs_iter:

        ## Text.
        if child.__class__ == CT_P:
            paragraph = Paragraph(child, document)
            contents.append(paragraph.text)

        ## Table.
        elif child.__class__ == CT_Tbl:
            table = Table(child, document)
            table_text = "\n".join(
                [
                    " | ".join(
                        [
                            cell.text.strip().replace("\n", " ")
                            for cell in row.cells
                            if (
                                cell.text is not None
                                and cell.text.strip() != ""
                            )
                        ]
                    )
                    for row in table.rows
                ]
            )
            table_text = "\n%s\n" % table_text
            contents.append(table_text)

    ## Join.
    content = "\n".join(contents)

    return content


def extract_pdf_content(path: str) -> str:
    """
    Extract content from `PDF` file.

    Parameters
    ----------
    path : File path.

    returns
    -------
    Content.
    """

    # Extract.
    document = pdfplumber_open(path)
    contents = [
        page.extract_text()
        for page in document.pages
    ]
    document.close()

    ## Join.
    content = "\n".join(contents)

    return content


def extract_file_content(path: str) -> str:
    """
    Extract content from `DOC` or `DOCX` or `PDF` file.

    Parameters
    ----------
    path : File path.

    returns
    -------
    Content.
    """

    # Handle parameter.
    _, suffix = os_splitext(path)
    suffix = suffix.lower()
    if suffix == ".doc":
        path = doc_to_docx(path)
        suffix = ".docx"

    # Extract.

    ## DOCX.
    if suffix == ".docx":
        content = extract_docx_content(path)

    ## PDF.
    elif suffix == ".pdf":
        content = extract_pdf_content(path)

    ## Throw exception.
    else:
        throw(value=suffix)

    return content