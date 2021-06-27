import cProfile
import argparse
from arg_orchestrator import arg_func_runner
from stdout import GREEN_CHECK, RED_OCT


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        result = []
        for d in num:
            while k and result and result[-1] > d:
                result.pop()
                k -= 1
            result.append(d)
        # [:None] is valid; saying if `-k` != 0
        # if result != []
        return ''.join(result).lstrip('0')[:-k or None] or '0'


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
    arg_func_runner(sol.removeKdigits, args=['4325043', 3], map=test_map)
