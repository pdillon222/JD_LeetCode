from typing import List

class Solution:
  def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    return [(num_candies + extraCandies >= max(candies)) for num_candies in candies]

if __name__=="__main__":
  sol = Solution()
  candies = [2,3,5,1,3]
  extra_candies = 3
  print(sol.kidsWithCandies(candies, extra_candies)) # => [true,true,true,false,true]
