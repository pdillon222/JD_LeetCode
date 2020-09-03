from typing import List

class Solution:
  def decompressRLElist(self, nums: List[int]) -> List[int]:
    dcmprsd_nums = []
    for i in range(len(nums)-1):
      if i == 0 or i%2 == 0:
        dcmprsd_nums.extend([nums[i+1] for num in range(nums[i])])
    return(dcmprsd_nums)

if __name__=="__main__":
  sol = Solution()
  nums = [1, 1, 2, 3] # => [1, 3, 3]
  print(sol.decompressRLElist(nums))
