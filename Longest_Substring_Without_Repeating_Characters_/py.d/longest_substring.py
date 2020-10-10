import cProfile
import argparse
from profiler import arg_func_runner


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substr_len = 0
        l_index = 0
        r_index = len(s) - 1
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
        # TODO - do stuff
        for char, indices in repeat_char_indices.items():
            counter = 0
            print(f'Repeating char "{char}" at -> {indices}')
            # iterate through lists of indices for repeat char, compare distance n[0] -> n[1]
            while counter < len(indices):
                if counter != len(indices) - 1:
                    print(f'{indices[counter]} -> {indices[counter + 1]}')
                else:
                    # if index is last in list; check distance from it to end of string
                    # determine whether or not duplicate chars are in this range
                    print(f'comparing index {indices[counter]} w/ end of string')
                    print(f'{indices[counter]} -> {len(s) - 1}')
                counter += 1
            print("--")
        ######
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
        "aab": 2,
        "abzdebbfgqbfwzmacb": 9
    }

    arg_func_runner(sol.lengthOfLongestSubstring, test_map, func_str="pwwkew")
    #sol.lengthOfLongestSubstring("")
