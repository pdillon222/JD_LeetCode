# -*- coding: UTF-8 -*-

from stdout import *
from typing import Callable, List


def map_cases_dict(test_map: dict, func: Callable[[type(abs)], None]) -> None:
    for k, v in test_map.items():
        func_result = func(k, brute_force) if brute_force else func(k)
        uni_char = GREEN_CHECK if func_result == test_map[k] else RED_OCT
        arg_str = f'{"#"*12} {func.__name__} => ({k}) {"#"*12}'
        print(f'{arg_str}\nTest input -> "{k}" results in mapped output {v}? '
              f'{bool_decorator(func_result == test_map[k])[-1]}\n'
              f'{" ":14}"{k}" => {func_result} {uni_char}\n{"#"*len(arg_str)}')

def map_cases(test_map: List, func: Callable[[type(abs)], None]) -> None:
    map_check = [len(case) == 2 and type(case[1]) == list
                 for case in test_map]
    if not all(map_check):
        print('[Error]: The following function result <-> arg mappings are faulty')
        for num, case in enumerate(map_check):
            if not case: print(test_map[num])
    for case in test_map:
        # iterate through all result & argument mappings:
        # pass in all args to `func` and confirm result matches case[0]
        result, args = case
        func_result = func(*args)
        uni_char = GREEN_CHECK if func_result == result else RED_OCT
        arg_str = f'{"#"*12} {func.__name__} => ({args}) {"#"*12}'
        print(f'{arg_str}\nTest input -> "{args}" results in mapped output {result}? '
              f'{bool_decorator(func_result == result)[-1]}\n'
              f'{" ":14}"{args}" => {func_result} {uni_char}\n{"#"*len(arg_str)}')
