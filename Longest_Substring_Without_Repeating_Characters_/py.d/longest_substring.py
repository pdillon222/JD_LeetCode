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
        visited_chars = [s[0]]
        max_substr_len = 0
        l_index = 0
        r_index = l_index + 1
        ############### Magic #################
        while l_index < len(s) :
            substr_len = len(s[l_index:r_index+1])
            while r_index < len(s):
                print(f'Testing substrings from index -> {l_index}')
                #r_index = l_index + 1
                print(f'checking {s[r_index]} in visited_chars')
                if s[r_index] in visited_chars:
                    print(f'Found char -> {s[r_index]} in visited_chars')
                    print(f'Substring -> {s[l_index:r_index+1]}')
                    if substr_len > max_substr_len:
                        print(f'Updating new max_substr_len -> {substr_len - 1}')
                        max_substr_len = substr_len - 1
                    l_index = r_index
                    break
                else:
                    # substr_char not found in visited_chars, append
                    print(f'Char -> {s[r_index]} NOT found in visited_chars; appending')
                    visited_chars.append(s[r_index])
                    if substr_len == len(s): return len(s)
                    substr_len += 1
                    print(f'new substr len -> {substr_len}')
                    if substr_len > max_substr_len:
                        print(f'Updating new max_substr_len -> {substr_len - 1}')
                        max_substr_len = substr_len - 1
                r_index += 1
            l_index += 1
            r_index = l_index + 1
            print('\n\n')
        ############# End Magic ###############
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
        "abzdebbfgqbfwzmacb": 7
    }

    #arg_func_runner(sol.lengthOfLongestSubstring, test_map, func_str="abcabcbb")
    arg_func_runner(sol.lengthOfLongestSubstring, test_map, func_str="abcdefg")
