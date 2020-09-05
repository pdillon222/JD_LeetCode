class Solution:
  def numberOfSteps (self, num: int) -> int:
    counter = 0
    while num > 0:
      if num % 2 == 0:
        num /= 2
      else:
        num -= 1
      counter += 1
    return int(counter)

if __name__=="__main__":
  solution = Solution()
  print(solution.numberOfSteps(123)) # => 12
