import cProfile
import argparse
from profiler import arg_func_runner


class Solution:
    @classmethod
    def string_from_file(cls, file_path):
        with open(file_path, 'r') as fp:
            return fp.read()

    @classmethod
    def repeat_char_dict(cls, s: str) -> dict:
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
        return repeat_char_indices

    def bruteForceLongestSubstring(self, s: str) -> int:
        max_substr_len = 0
        for i in range(len(s)):
            #if len(s[i:]) <= max_substr_len:
                #return max_substr_len
            for j in range(i+1, len(s)+1):
                if len(s[i:j]) == len(set(s[i:j])) and \
                len(s[i:j]) > max_substr_len:
                    max_substr_len = len(s[i:j])
        print(max_substr_len)
        return max_substr_len

    def lengthOfLongestSubstring(self, s: str, brute_force=False) -> int:
        if brute_force:
            return self.bruteForceLongestSubstring(s)
        max_substr_len = 0
        print(s)
        repeat_char_indices = __class__.repeat_char_dict(s)
        # if each index list has <= 1 value, no repeat chars -> return len(s)
        if set([len(indices) for indices
            in repeat_char_indices.values()]) == {1}: return len(s)
        print(repeat_char_indices)
        ###############

        ###############
        print(max_substr_len)
        return max_substr_len


if __name__=="__main__":
    sol = Solution()
    test_map = {
        "abcabcbb": 3,
        "bbbbb": 1,
        "pwwkew": 3,
        "abcdefg": 7,
        "aab": 2,
        "abzdebbfgqbfwzmacb": 9
    }

    arg_func_runner(sol.lengthOfLongestSubstring, test_map, func_str="abcabcbb")
