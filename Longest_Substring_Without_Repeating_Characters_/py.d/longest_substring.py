import cProfile
import argparse
from profiler import arg_func_runner
from stdout import GREEN_CHECK, RED_OCT


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
        if not s: return 0
        visited_chars = [s[0]]
        max_substr_len = 0
        l_index = 0
        r_index = l_index + 1
        ############### Magic #################
        while (l_index < len(s)) and (r_index < len(s)):
            crnt_substr_len = len(s[l_index:r_index+1])
            print(f'checking substring -> {s[l_index:r_index+1]}, length == {crnt_substr_len}')
            if s[r_index] in visited_chars:
                print(f'found char -> {s[r_index]} in visited_chars {RED_OCT}; setting l_index -> {r_index}\n')
                l_index = r_index
                r_index = l_index
                crnt_substr_len = 0
                visited_chars = [s[l_index]]
            else:
                print(f'char -> {s[r_index]} not found in visited_chars {GREEN_CHECK}; appending and incrementing crnt_substr')
                visited_chars.append(s[r_index])
            if crnt_substr_len > max_substr_len:
                print(f'Substring {s[l_index:r_index+1]} of length {crnt_substr_len} > max_substr_len {max_substr_len} -> {GREEN_CHECK}{GREEN_CHECK}')
                max_substr_len = crnt_substr_len
            r_index += 1
        ############# End Magic ###############
        if not max_substr_len and visited_chars: max_substr_len = 1
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
        "dvdf": 3
    }

    arg_func_runner(sol.lengthOfLongestSubstring, test_map, func_str="dvdf")
    #arg_func_runner(sol.lengthOfLongestSubstring, test_map, func_str="abcdefg")
