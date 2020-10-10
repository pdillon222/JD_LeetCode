import cProfile
import argparse
from profiler import arg_func_runner


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substr_len = 0
        l_index = 0
        r_index = len(s) - 1
        #print(s[l_index:r_index + 1]) # the full string
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
        # if each index list has <= 1 value, no repeat chars -> return len(s)
        if set([len(indices) for indices in repeat_char_indices.values()]) == {1}:
            return len(s)

        for char, indices in repeat_char_indices.items():
            counter = 0
            print(f'"{char}" -> {indices}')
            # check substring from s[0:indices[0]] - if counter == 0
            # check substring from s[indices[counter]:indices[counter + 1]]
            # check substring from s[indices[counter]:len(s)] - if counter == len(indices) - 1
            while counter < len(indices):
                if counter == 0:
                    print(s[0:])
                    pass
                elif counter == len(counter) - 1:
                    pass
                else:
                    # compare substring between indices
                    pass

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
