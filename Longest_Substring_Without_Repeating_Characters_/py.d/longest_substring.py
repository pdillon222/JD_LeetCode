import cProfile
import argparse
from profiler import arg_func_runner

''' - Brute force method: fails LeetCode time constraint
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
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # find all repeating chars
        # create map of repeating chars to list of their indices
        # for those chars w/ multiple indices:
          # measure the distance up to the end of the string
          # see if in that range - there lies repeated chars (by comparing dict values w/ > 1 list entries)
        max_substr_len = 0
        repeat_char_indices = {}
        counter = 0
        while counter < len(s):
            if s[counter] not in repeat_char_indices:
                # initialize key w/ list containing index of char
                repeat_char_indices[s[counter]] = [counter]
            else:
                # append index to repeat_char_indices[s]
                repeat_char_indices[s[counter]].append(counter)
            counter += 1
        if set([len(indices) for indices in repeat_char_indices.values()]) == {1}:
            max_substr_len = len(s)
            return max_substr_len
        for indices in repeat_char_indices.values():
            counter = 0
            if len(indices) > 1:
                while counter < len(indices) - 1:
                    if indices[counter + 1] - indices[counter] > max_substr_len:
                        max_substr_len = indices[counter + 1] - indices[counter]
                    counter += 1
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
        "pwwkew": 3,
        "abcdefg": 7,
        "aab": 2
    }

    arg_func_runner(sol.lengthOfLongestSubstring, test_map, func_str="pwwkew")
    #sol.lengthOfLongestSubstring("")
