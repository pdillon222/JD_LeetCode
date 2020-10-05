import cProfile
import argparse
from test_assertions import map_cases


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substr_len = 0
        left_index = 0

        ''' FAIL -> only compares l_index w/ each char to the right
        #for i in range(0, len(s)):
        while left_index < len(s):
            right_index = left_index + 1
            dup_char_flag = False
            print(f'Starting at index -> {left_index} == {s[left_index]}')
            #for j in range(i+1, len(s)):
            while right_index < len(s) and not dup_char_flag:
                print(f'{s[left_index]} => {s[right_index]}')
                dup_char_flag = s[left_index] == s[right_index]
                substr_len = len(s[left_index:right_index+1])
                right_index += 1
            if not dup_char_flag and max_substr_len < substr_len:
                print(f'Adding substr -> "{s[left_index:right_index]}"')
                max_substr_len = substr_len
            print('\n')
            left_index += 1
        '''
        print(max_substr_len)
        return max_substr_len

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
