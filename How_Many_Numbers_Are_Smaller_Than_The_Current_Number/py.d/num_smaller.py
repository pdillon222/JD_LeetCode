from typing import List

class Solution:
  def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    compare_dict = {key:"" for key in set(nums)}
    compare_array = []
    for num in nums:
      if not compare_dict[num]:
        compare_dict[num] = len([_num for _num in nums if _num < num])
      compare_array.append(compare_dict[num])
    return compare_array

if __name__=="__main__":
  sol = Solution()
  print(sol.smallerNumbersThanCurrent([8,1,2,2,3])) # => [4,0,1,1,3]
