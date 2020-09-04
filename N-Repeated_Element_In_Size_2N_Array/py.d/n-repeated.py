class Solution:
  def repeatedNTimes(self, A):
    counts = {}
    for i in A:
      if i not in counts:
        counts[i] = 1
      else:
        counts[i] += 1
      if counts[i] == len(A) / 2:
        return i

if __name__=="__main__":
  sol = Solution()
  print(Solution.repeatedNTimes([1,2,3,3])) # => 3
