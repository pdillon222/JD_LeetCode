# -*- coding: UTF-8 -*-

from typing import Tuple


GREEN_CHECK = u'\u2705'
RED_OCT = u'\U0001F534'


def unicode_range(start: int, end: int) -> None:
    for i in range(start, end):
        print(str(i) + " -> " + (b'\\u%d' % i).decode('raw_unicode_escape'))

def bool_decorator(bool_val: bool) -> tuple:
    return (bool_val,
            "\033[38;5;27m\033[48;5;83m{}\033[0m".format(str(bool_val))) \
            if bool_val else (bool_val,
            "\033[38;5;86m\033[48;5;9m{}\033[0m".format(str(bool_val)))


if __name__=="__main__":
    print(bool_decorator(True)[-1])
    print(bool_decorator(False)[-1])
