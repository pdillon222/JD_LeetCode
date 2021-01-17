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
        index = 1
        if k >= n: return '0'
        if k == 0: return num
        num_stack = []
        while index < n and k:
            print(f'char -> {num[index]}; {k} remaining chars to remove')
            if int(num[index]) >= int(num[index - 1]):
                print(f'Adding {num[index]} to stack')




if __name__=="__main__":
    sol = Solution()
    test_map = [
        ('1219', [3, '1432219']),
        ('200', [1, '10200']),
        ('0', [2, '10'])
    ]
    test_mapII = [
        ('2043', [3, '4325043']),
        ('221', [5, '765028321']),
        ('1118', [2, '121198'])
    ]
    arg_func_runner(sol.removeKdigits, args=['16374112', 2], map=test_map)  # "134112"
