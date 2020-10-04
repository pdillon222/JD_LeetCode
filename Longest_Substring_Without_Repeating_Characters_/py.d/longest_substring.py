import cProfile
import argparse
from test_assertions import map_cases

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print('who run it?...')
        return len(s)


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
            print("Running function w/ no args")
            sol.lengthOfLongestSubstring("abcabcbb")
