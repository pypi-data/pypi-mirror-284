# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2023-06-16 13:49:33
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Table methods.
"""


from typing import Any, List, Dict, Iterable, Literal, Optional, Union, overload
from os.path import abspath as os_abspath
from pandas import DataFrame, ExcelWriter, isnull
from sqlalchemy.engine.cursor import CursorResult

from .ros import RFile
from .rtext import to_json, to_text
from .rtime import time_to


__all__ = (
    "fetch_table",
    "fetch_dict",
    "fetch_list",
    "fetch_df",
    "fetch_json",
    "fetch_text",
    "fetch_sql",
    "fetch_html",
    "fetch_csv",
    "fetch_excel"
)

# Table format data type.
Table = Union[List[Dict], Dict, CursorResult, DataFrame]


def fetch_table(
    data: Union[Table, Iterable[Iterable]],
    fields: Optional[Iterable] = None
) -> List[Dict]:
    """
    Fetch data to table in `List[Dict]` format, keys and keys sort of the dictionary are the same.

    Parameters
    ----------
    data : Table format data.
    fields : Table fields.
        - `None` : Infer.
        - `Iterable` : Use values in Iterable.

    Returns
    -------
    Table in `List[Dict]` format.
    """

    # Convert.

    ## From CursorResult object.
    if isinstance(data, CursorResult):
        if fields is None:
            fields = data.keys()
        data_table = [
            dict(zip(fields, row))
            for row in data
        ]

    ## From DataFrame object.
    elif data.__class__ == DataFrame:
        data_df = fetch_df(data, fields)
        fields = data_df.columns
        data_table = [
            dict(zip(
                fields,
                [
                    None if isnull(value) else value
                    for value in row
                ]
            ))
            for row in data_df.values
        ]

    ## From other object.
    else:
        data_df = fetch_df(data, fields)
        data_table = fetch_table(data_df)

    return data_table


@overload
def fetch_dict(
    data: Union[Table, Iterable[Iterable]],
    key_field: Union[int, str] = 0,
    val_field: None = None
) -> Dict[Any, Dict]: ...

@overload
def fetch_dict(
    data: Union[Table, Iterable[Iterable]],
    key_field: Union[int, str] = 0,
    val_field: Union[int, str] = None
) -> Dict: ...

def fetch_dict(
    data: Union[Table, Iterable[Iterable]],
    key_field: Union[int, str] = 0,
    val_field: Optional[Union[int, str]] = None
) -> Union[Dict[Any, Dict], Dict]:
    """
    Fetch result as dictionary.

    Parameters
    ----------
    data : Table format data.
    key_field : Key field of dictionary.
        - `int` : Subscript index.
        - `str` : Name index.

    val_field : Value field of dictionary.
        - `None` : All fields except key.
        - `int` : Subscript index.
        - `str` : Name index.

    Returns
    -------
    Dictionary.
    """

    # Handle parameter.
    data = fetch_table(data)

    ## Check parameter.
    if len(data) == 0:
        return {}

    # Get fields.
    fields = list(data[0].keys())
    if key_field.__class__ == int:
        key_field = fields[key_field]
    if val_field.__class__ == int:
        val_field = fields[val_field]

    # Convert.

    ## Value is all fields except key.
    if val_field is None:
        data_dict = {
            row[key_field]: {
                key: value
                for key, value in row.items()
                if key != key_field
            }
            for row in data
        }

    ## Value is one field.
    else:
        data_dict = {
            row[key_field]: row[val_field]
            for row in data
        }

    return data_dict


def fetch_list(
    data: Union[Table, Iterable[Iterable]],
    field: Union[int, str] = 0,
) -> List:
    """
    Fetch result as list.

    Parameters
    ----------
    data : Table format data.
    field : Field of value.
        - `int` : Subscript index.
        - `str` : Name index.

    Returns
    -------
    List.
    """

    # Handle parameter.
    data = fetch_table(data)

    ## Check parameter.
    if len(data) == 0:
        return []

    # Get fields.
    fields = list(data[0].keys())
    if field.__class__ == int:
        field = fields[field]

    # Convert.
    data_list = [
        row[field]
        for row in data
    ]

    return data_list


def fetch_df(
    data: Union[Table, Iterable[Iterable]],
    fields: Optional[Iterable] = None
) -> DataFrame:
    """
    Fetch data to table of `DataFrame` object.

    Parameters
    ----------
    data : Table format data.
    fields : Table fields.
        - `None` : Infer.
        - `Iterable` : Use values in Iterable.

    Returns
    -------
    DataFrame object.
    """

    # Convert.

    ## From CursorResult object.
    if isinstance(data, CursorResult):
        if fields is None:
            fields = data.keys()
        data_df = DataFrame(data, columns=fields)
        data_df = data_df.convert_dtypes()

    ## From DataFrame object.
    elif data.__class__ == DataFrame:
        data_df = data.convert_dtypes()
        if fields is not None:
            data_df.columns = fields

    ## From other object.
    else:
        if data.__class__ == dict:
            data = [data]
        data_df = DataFrame(data, columns=fields)
        data_df = data_df.convert_dtypes()

    return data_df


def fetch_json(
    data: Union[Table, Iterable[Iterable]],
    fields: Optional[Iterable] = None,
    compact: bool = True
) -> str:
    """
    Fetch data to JSON string.

    Parameters
    ----------
    data : Table format data.
    fields : Table fields.
        - `None` : Infer.
        - `Iterable` : Use values in Iterable.

    compact : Whether compact content.

    Returns
    -------
    JSON string.
    """

    # Handle parameter.
    data = fetch_table(data, fields)

    # Convert.
    string = to_json(data, compact)

    return string


def fetch_text(
    data: Union[Table, Iterable[Iterable]],
    fields: Optional[Iterable] = None,
    width: int = 100
) -> str:
    """
    Fetch data to text.

    Parameters
    ----------
    data : Table format data.
    fields : Table fields.
        - `None` : Infer.
        - `Iterable` : Use values in Iterable.

    width : Format width.

    Returns
    -------
    Formatted text.
    """

    # Handle parameter.
    data = fetch_table(data, fields)

    # Convert.
    text = to_text(data, width)

    return text


def fetch_sql(
    data: Union[Table, Iterable[Iterable]],
    fields: Optional[Iterable] = None
) -> str:
    """
    Fetch data to SQL string.

    Parameters
    ----------
    data : Table format data.
    fields : Table fields.
        - `None` : Infer.
        - `Iterable` : Use values in Iterable.

    Returns
    -------
    SQL string.
    """

    # Get fields of table.
    if isinstance(data, CursorResult):
        if fields is None:
            fields = data.keys()
    else:
        data = fetch_table(data, fields)
        fields = data[0].keys()

    # Generate SQL.
    sql_rows_values = [
        [
            repr(time_to(value, raising=False))
            if value is not None
            else "NULL"
            for value in row
        ]
        for row in data
    ]
    sql_rows = [
        "SELECT " + ",".join(row_values)
        for row_values in sql_rows_values
    ]
    sql_row_first = "SELECT " + ",".join(
        [
            f"{value} AS `{key}`"
            for key, value in list(zip(fields, sql_rows_values[0]))
        ]
    )
    sql_rows[0] = sql_row_first
    data_sql = " UNION ALL ".join(sql_rows)

    return data_sql


def fetch_html(
    data: Union[Table, Iterable[Iterable]],
    fields: Optional[Iterable] = None
) -> str:
    """
    Fetch data to HTML string.

    Parameters
    ----------
    data : Table format data.
    fields : Table fields.
        - `None` : Infer.
        - `Iterable` : Use values in Iterable.

    Returns
    -------
    HTML string.
    """

    # Handle parameter.
    data_df = fetch_df(data, fields)

    # Convert.
    data_html = data_df.to_html(col_space=50, index=False, justify="center")

    return data_html


def fetch_csv(
    data: Union[Table, Iterable[Iterable]],
    path: str = "data.csv",
    fields: Optional[Iterable] = None
) -> str:
    """
    Fetch data to save CSV format file.
    When file exist, then append data.

    Parameters
    ----------
    data : Table format data.
    path : File save path.
    fields : Table fields.
        - `None` : Infer.
        - `Iterable` : Use values in Iterable.

    Returns
    -------
    File absolute path.
    """

    # Handle parameter.
    data_df = fetch_df(data, fields)
    rfile = RFile(path)
    if rfile:
        header = False
    else:
        header = True

    # Save file.
    data_df.to_csv(rfile.path, header=header, index=False, mode="a")

    return rfile.path


def fetch_excel(
    data: Union[Table, Iterable[Iterable]],
    path: str = "data.xlsx",
    group_field: Optional[str] = None,
    sheets_set: Dict[Union[str, int], Dict[Literal["name", "index", "fields"], Any]] = {}
) -> str:
    """
    Fetch data to save Excel format file and return sheet name and sheet data.
    When file exist, then rebuild file.

    Parameters
    ----------
    data : Table format data.
    path : File save path.
    group_field : Group filed.
    sheets_set : Set sheet new name and sort sheet and filter sheet fields,
        key is old name or index, value is set parameters.
        - Parameter `name` : Set sheet new name.
        - Parameter `index` : Sort sheet.
        - Parameter `fields` : Filter sheet fields.

    Returns
    -------
    File absolute path.

    Examples
    --------
    >>> data = [
    ...     {'id': 1, 'age': 21, 'group': 'one'},
    ...     {'id': 2, 'age': 22, 'group': 'one'},
    ...     {'id': 3, 'age': 23, 'group': 'two'}
    ... ]
    >>> sheets_set = {
    ...     'one': {'name': 'age', 'index': 2, 'fields': ['id', 'age']},
    ...     'two': {'name': 'id', 'index': 1, 'fields': 'id'}
    ... }
    >>> fetch_excel(data, 'file.xlsx', 'group', sheets_set)
    """

    # Handle parameter.
    if data.__class__ != DataFrame:
        data = fetch_df(data)
    path = os_abspath(path)

    # Generate sheets.
    if group_field is None:
        data_group = (("Sheet1", data),)
    else:
        data_group = data.groupby(group_field)
    sheets_table_before = []
    sheets_table_after = []
    for index, sheet_table in enumerate(data_group):
        sheet_name, sheet_df = sheet_table
        if group_field is not None:
            del sheet_df[group_field]
        if sheet_name in sheets_set:
            sheet_set = sheets_set[sheet_name]
        elif index in sheets_set:
            sheet_set = sheets_set[index]
        else:
            sheets_table_after.append((sheet_name, sheet_df))
            continue
        if "name" in sheet_set:
            sheet_name = sheet_set["name"]
        if "fields" in sheet_set:
            sheet_df = sheet_df[sheet_set["fields"]]
        if "index" in sheet_set:
            sheets_table_before.append((sheet_set["index"], (sheet_name, sheet_df)))
        else:
            sheets_table_after.append((sheet_name, sheet_df))
    sort_func = lambda item: item[0]
    sheets_table_before.sort(key=sort_func)
    sheets_table = [sheet_table for sheet_index, sheet_table in sheets_table_before] + sheets_table_after

    # Save file.
    excel = ExcelWriter(path)
    for sheet_name, sheet_df in sheets_table:
        sheet_df.to_excel(excel, sheet_name, index=False)
    excel.close()

    return path