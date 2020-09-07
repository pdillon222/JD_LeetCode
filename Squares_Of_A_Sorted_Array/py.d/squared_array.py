from typing import List

class Solution:
  def sortedSquares(array: List) -> List:
    return sorted([num**2 for num in array])

if __name__=="__main__":
  sol = Solution()
  print(sol.sortedSquares([-4,-1,0,3,10])) # => [0,1,9,16,100]
