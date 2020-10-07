import cProfile
import argparse
from profiler import arg_func_runner


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substr_len = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if len(s[i:j]) == len(set(s[i:j])) and \
                len(s[i:j]) > max_substr_len:
                    max_substr_len = len(s[i:j])
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

    arg_func_runner(sol.lengthOfLongestSubstring, test_map, func_str="abcabcbb")
