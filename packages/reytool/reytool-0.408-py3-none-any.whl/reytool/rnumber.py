# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time    : 2023-04-22 22:32:34
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Number methods.
"""


from typing import Any, Tuple, Union

from .rsystem import throw, is_number_str


__all__ = (
    "digits",
    "number",
    "number_ch"
)


def digits(number: Union[int, float]) -> Tuple[int, int]:
    """
    Judge the number of integer digits and decimal digits.

    Parameters
    ----------
    number : Number to judge.

    Returns
    -------
    Integer digits and decimal digits.
    """

    # Handle parameter.
    number_str = str(number)

    # Get digits.
    if "." in number_str:
        int_str, dec_str = number_str.split(".")
        int_digits = len(int_str)
        dec_digits = len(dec_str)
    else:
        int_digits = len(number_str)
        dec_digits = 0

    return int_digits, dec_digits


def number(
    string: str,
    raising: bool = True
) -> Any:
    """
    convert string to number.

    Parameters
    ----------
    string : String.
    raising : When parameter `string` value error, whether throw exception, otherwise return original value.

    Returns
    -------
    Converted number.
    """

    # Number.
    if is_number_str(string):
        if "." in string:
            number = float(string)
        else:
            number = int(string)
        return number

    # Throw exception.
    elif raising:
        throw(ValueError, string)

    return string


def number_ch(number: int) -> str:
    """
    Convert number to chinese number.

    Parameters
    ----------
    number : Number to convert.

    Returns
    -------
    Chinese number.
    """

    # Import.
    from .rregex import sub_batch

    # Set parameter.
    map_digit = {
        "0": "零",
        "1": "一",
        "2": "二",
        "3": "三",
        "4": "四",
        "5": "五",
        "6": "六",
        "7": "七",
        "8": "八",
        "9": "九",
    }
    map_digits = {
        0: "",
        1: "十",
        2: "百",
        3: "千",
        4: "万",
        5: "十",
        6: "百",
        7: "千",
        8: "亿",
        9: "十",
        10: "百",
        11: "千",
        12: "万",
        13: "十",
        14: "百",
        15: "千",
        16: "兆"
    }

    # Handle parameter.
    number_str = str(number)

    # Replace digit.
    for digit, digit_ch in map_digit.items():
        number_str = number_str.replace(digit, digit_ch)

    # Add digits.
    number_list = []
    for index, digit_ch in enumerate(number_str[::-1]):
        digits_ch = map_digits[index]
        number_list.insert(0, digits_ch)
        number_list.insert(0, digit_ch)
    number_str = "".join(number_list)

    # Delete redundant content.
    number_str = sub_batch(
        number_str,
        ("(?<=零)[^万亿兆]", ""),
        ("零+", "零"),
        ("零(?=[万亿兆])", "")
    )
    if number_str.startswith("一十"):
        number_str = number_str[1:]
    if number_str.endswith("零"):
        number_str = number_str[:-1]

    return number_str