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
        index = 0
        while index < n - 1 and k:
            if int(num[index]) > int(num[index + 1]):
                print(f'removing index {index} -> "{num[index]}"')
                remove_indices.append(index)
                k -= 1
            index += 1
        # edge cases:
        # - len(remove_indices) == 0
        # - len(remove_indices) < k
        reduced_string =  ''.join([num[index] for index in range(len(num))
                                  if index not in remove_indices])
        print(reduced_string)
        return reduced_string.lstrip('0')


if __name__=="__main__":
    sol = Solution()
    test_map = [
        ('1219', ['1432219', 3]),
        ('200', ['10200', 1]),
        ('0', ['10', 2])
    ]
    test_mapII = [
        ('2043', ['4325043', 3]),
        ('221', ['765028321', 5]),
        ('1118', ['121198', 2])
    ]
    arg_func_runner(sol.removeKdigits, args=['16374112', 3], map=test_map)  # "13112"
