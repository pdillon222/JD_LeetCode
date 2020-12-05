import argparse
from test_assertions import map_cases
from typing import List, Callable, TypeVar

ArgsList = TypeVar('ArgsList')

ARGS_LIST = [
    '--profile',
    '--test-cases',
    '--brute-force'
]

def argument_parser() -> ArgsList:
    parser = argparse.ArgumentParser()
    for arg in ARGS_LIST:
        parser.add_argument(arg, action='store_true')
    return parser.parse_args()

def arg_func_runner(func: Callable,
                    test_map: dict,
                    func_str: str = None,
                    func_int: int = None,
                    func_list: List = None,
                    func_dict: dict = None,
                    brute_force: bool = False) -> None:
    args = argument_parser()
    brute_force = True if args.brute_force else False
    if args.test_cases:
        map_cases(test_map, func, brute_force)
    else:
        if args.profile:
            # run code profiling:
            #cProfile.runctx('g(x,y)', {'x': n, 'y': m, 'g': func},{})
            profile_str = " Profiling function code "
            delim = f'{"=" * (26 + len(profile_str))}'
            print(f'{delim}\n{"=":13}{profile_str}{" ":12}=\n{delim}')
        else:
            funcout = "Running function w/ no args"
            print(f'{"-" * len(funcout)}\n{funcout}\n{"-" * len(funcout)}')
            args_list = [arg for arg in [func_str, func_int, func_list, func_dict, brute_force] if arg]
            func(*args_list)
