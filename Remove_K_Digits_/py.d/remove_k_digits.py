import cProfile
import argparse
from arg_orchestrator import arg_func_runner
from stdout import GREEN_CHECK, RED_OCT


class Solution:
    @classmethod
    def buildLowestNumString(cls, str_num: str, n: int, res: str) -> str:
        if n == 0: return str_num
        length = len(str_num)
        if length <= n: return res
        min_index = 0
        for i in range(1, n):
            if str_num[i] < str_num[min_index]: min_index = i
        res += str_num[min_index]
        print(f'new value of res_str -> {res}')
        substring = str_num[min_index + 1:]
        print(f'new substring -> {substring}')
        return __class__.buildLowestNumString(substring, n - min_index, res)

    def removeKdigits(self, num: str, k: int) -> str:
        result = __class__.buildLowestNumString(num, k, "")
        print(result)
        while result[0] == '0': result = result[1:]
        return '0' if result == '' else result


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
    arg_func_runner(sol.removeKdigits, args=['1234567890', 9], map=test_map[0:1])#[-2:])  # "0"
