import cProfile
import argparse
from arg_orchestrator import arg_func_runner
from stdout import GREEN_CHECK, RED_OCT


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # if num in ascending order -> remove last k digits
        # conversely - in descending order -> first k digits
        # everything else
        n = len(num)
        if k >= n: return '0'
        if k == 0: return num
        remove_indices = []
        index = 1
        while index < n  and k:
            if int(num[index - 1]) > int(num[index]):
                print(f'removing index {index - 1} -> "{num[index - 1]}"')
                remove_indices.append(index - 1)
                k -= 1
            index += 1
        # edge cases:
        # - len(remove_indices) == 0 # indicates all nums are ascending -> thus we chop off the end
        # - len(remove_indices) < k # indicates remaining chars are ascending -> thus we chop off the end

        # if k leftover - we simply subtract it from remaining range
        print(f'remaining value of k -> {k}')
        string_range = range(k, len(num)) if k else range(len(num) - k)
        reduced_string = ''.join([num[index] for index in string_range
                                 if index not in remove_indices])
        zero_check = all([_char == '0' for _char in reduced_string])
        if zero_check:
            return '0'
        return reduced_string.lstrip('0')


if __name__=="__main__":
    sol = Solution()
    test_map = [
        ('1219', ['1432219', 3]),
        ('200', ['10200', 1]),
        ('0', ['10', 2]),
        ('0', ['1234567890', 9]), # problem
        ('11', ['112', 1])
    ]
    test_mapII = [
        ('2043', ['4325043', 3]),
        ('221', ['765028321', 5]),
        ('1118', ['121198', 2])
    ]
    arg_func_runner(sol.removeKdigits, args=['1234567890', 9], map=test_map[-2:])  # "0"
