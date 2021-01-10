import cProfile
import argparse
from arg_orchestrator import arg_func_runner
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

    def lengthOfLongestSubstring(self, s: str) -> int:
        # slow 'window sliding' method -> O(n^3)
        max_substr_len = 0
        ############### Magic #################
        for i in range(len(s)):
            print('resetting visited_chars to array of 0s')
            visited_chars = [0] * 256
            for j in range(i, len(s)):
                print(f'Checking substring -> {s[i:j+1]}')
                # stop checking current substr if current char is visited
                if (visited_chars[ord(s[j])] == True):
                    print(f'Char -> {s[j]} is a repeating char - breaking loop')
                    break
                # if not visited - update max substr len if current substr is >
                # mark the current char as visited
                else:
                    print(f'Char -> {s[j]} is not a repeating char - checking max_substr_len')
                    max_substr_len = max(max_substr_len, j - i + 1)
                    visited_chars[ord(s[j])] = True
            # remove first char of previous window
            print(f'Outside of inner loop, removing char -> {s[i]} from visited chars\n')
        ############# End Magic ###############
        print(f'Returning max_subtr_len -> {max_substr_len}')
        return max_substr_len

    def lengthOfLongestSubstringLinearTime(self, s: str) -> int:
        # Initialize the last index array as -1, -1 is used to store
        # last index of every character
        lastIndex = [-1] * 256
        n = len(s)
        max_substr_len = 0   # Result
        i = 0
        for j in range(0, n):
            # Find the last index of str[j]
            # Update i (starting index of current window)
            # as maximum of current value of i and last
            # index plus 1
            i = max(i, lastIndex[ord(s[j])] + 1);
            # Update result if we get a larger window
            max_substr_len =  max(max_substr_len, j - i + 1)
            # Update last index of j.
            lastIndex[ord(s[j])] = j;
        return max_substr_len

    def lengthOfLongestSubstring24msSolution(self, s: str) -> int:
        # code profiled at 24ms against LeetCode test-cases
        if len(s)<2:
            return len(s)
        long_str=''
        len_val=0
        for i in range(len(s)):
            if s[i] not in long_str:
                long_str+=s[i]
            else:
                ref_ind=long_str.find(s[i])
                len_val=max(len_val,len(long_str))
                long_str=long_str[ref_ind+1:]+s[i]
        return max(len_val,len(long_str))


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
    arg_func_runner(sol.lengthOfLongestSubstring, args=["abcdefg"], map=test_map)
