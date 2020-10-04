import cProfile
import argparse
from test_assertions import map_cases


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substr_len = 0
        index_l = 0
        # brute-force: start at index[n], compare index[n+1]

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    for arg in ['--profile', '--test-cases']:
        parser.add_argument(arg, action='store_true')
    args = parser.parse_args()
    sol = Solution()
    test_map = {
        "abcabcbb": 3,
        "bbbbb": 1,
        "pwwkew": 3
    }

    if args.test_cases:
        map_cases(test_map, sol.lengthOfLongestSubstring)
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
            sol.lengthOfLongestSubstring("abcabcbb")
