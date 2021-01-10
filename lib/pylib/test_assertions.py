# -*- coding: UTF-8 -*-

from stdout import *
from typing import Callable

# Callable[[Arg1Type, Arg2Type], ReturnType]

'''
 TODO - rework to use new map data structure:
 considerations:
   - list of tuples -> (result, [args])
   - list of dicts -> {'res': val, 'args': [args]}
 construct a helper function - for creating the data structure:
   - func(res_list: list, args_list: list[list])
'''

def map_cases(test_map: dict, func: Callable[[type(abs)], None]) -> None:
    for k, v in test_map.items():
        func_result = func(k, brute_force) if brute_force else func(k)
        uni_char = GREEN_CHECK if func_result == test_map[k] else RED_OCT
        arg_str = f'{"#"*12} {func.__name__} => ({k}) {"#"*12}'
        print(f'{arg_str}\nTest input -> "{k}" results in mapped output {v}? '
              f'{bool_decorator(func_result == test_map[k])[-1]}\n'
              f'{" ":14}"{k}" => {func_result} {uni_char}\n{"#"*len(arg_str)}')
