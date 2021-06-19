import argparse
from test_assertions import map_cases
from typing import List, Callable, TypeVar

ArgsList = TypeVar('ArgsList')

ARGS_LIST = [
    '--profile',
    '--test-cases'
]

def argument_parser() -> ArgsList:
    parser = argparse.ArgumentParser()
    for arg in ARGS_LIST:
        parser.add_argument(arg, action='store_true')
    return parser.parse_args()

def arg_func_runner(func: Callable, *args, **kwargs) -> None:
    parsed_args = argument_parser()
    if parsed_args.test_cases:
        test_map = kwargs.get('map')
        assert test_map, \
            '[Error]: "--test-cases" arg requires map of arg <-> return vals'
        map_cases(test_map, func)
    else:
        if parsed_args.profile:
            # run code profiling:
            #cProfile.runctx('g(x,y)', {'x': n, 'y': m, 'g': func},{})
            profile_str = " Profiling function code "
            delim = f'{"=" * (26 + len(profile_str))}'
            print(f'{delim}\n{"=":13}{profile_str}{" ":12}=\n{delim}')
        else:
            positional_args = kwargs.get('args')
            assert positional_args, \
                f'[Error]: {func} requires a list of arguments'
            funcout = f'Running function w/ positional args -> '
            funcout += f'"{", ".join([str(arg) for arg in positional_args])}"'
            print(f'{"-" * len(funcout)}\n{funcout}\n{"-" * len(funcout)}')
            res = func(*positional_args)
            print(f'Result => {res}')
