import argparse
from test_assertions import map_cases
from typing import List, Callable, TypeVar

ArgsList = TypeVar('ArgsList')

ARGS_LIST = [
    '--profile',
    '--test-cases',
    '--helper'
]

def argument_parser() -> ArgsList:
    parser = argparse.ArgumentParser()
    for arg in ARGS_LIST:
        parser.add_argument(arg, action='store_true')
    print(parser.parse_args())
    return parser.parse_args()

def arg_func_runner(func: Callable,
                    test_map: dict,
                    func_str: str = None,
                    func_int: int = None,
                    func_list: List = None,
                    func_dict: dict = None) -> None:
    args = argument_parser()
    if args.test_cases:
        map_cases(test_map, func)
    else:
        if args.profile:
            # run code profiling:
            #cProfile.runctx('g(x,y)', {'x': n, 'y': m, 'g': func},{})
            profile_str = " Profiling function code "
            delim = f'{"=" * (26 + len(profile_str))}'
            print(f'{delim}\n{"=":13}{profile_str}{" ":12}=\n{delim}')
        else:
            func_str = "Running function w/ no args"
            print(f'{"-" * len(func_str)}\n{func_str}\n{"-" * len(func_str)}')
            args_list = 
            func(*args_list)
