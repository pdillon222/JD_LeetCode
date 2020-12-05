# -*- coding: UTF-8 -*-

from stdout import *
from typing import Callable

# Callable[[Arg1Type, Arg2Type], ReturnType]

def map_cases(test_map: dict, func: Callable[[type(abs)], None], brute_force: bool = False) -> None:
    for k, v in test_map.items():
        func_result = func(k, brute_force) if brute_force else func(k)
        uni_char = GREEN_CHECK if func_result == test_map[k] else RED_OCT
        arg_str = f'{"#"*12} {func.__name__} => ({k}) {"#"*12}'
        print(f'{arg_str}\nTest input -> "{k}" results in mapped output {v}? '
              f'{bool_decorator(func_result == test_map[k])[-1]}\n'
              f'{" ":14}"{k}" => {func_result} {uni_char}\n{"#"*len(arg_str)}')
