# -*- coding: UTF-8 -*-

from stdout import *
from typing import Callable

# Callable[[Arg1Type, Arg2Type], ReturnType]

def map_cases(test_map: dict, func: Callable[[type(abs)], None]) -> None:
    for k, v in test_map.items():
        func_result = func(k)
        uni_char = GREEN_CHECK if func_result == test_map[k] else RED_OCT
        print(f'Test input -> "{k}" results in mapped output {v}? '
              f'{bool_decorator(func_result == test_map[k])[-1]}\n'
              f'{" ":14}"{k}" => {func_result} {uni_char}')
