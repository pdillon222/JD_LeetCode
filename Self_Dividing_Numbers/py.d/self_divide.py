from typing import List

class Solution:
  def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    zero_mods = []
    for i in range(left, right + 1):
      mod_flag = True
      for num in [int(j) for j in str(i)]:
        if num == 0 or i % num != 0:
          mod_flag = False
      if mod_flag:
        zero_mods.append(i)
    return zero_mods

if __name__=="__main__":
  sol = Solution()
  print(sol.selfDividingNumbers(1, 22)) # => [1,2,3,4,5,6,7,8,9,11,12,15,22]
