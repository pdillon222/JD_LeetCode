class Solution:
  def reverseWords(self, s: str) -> str:
    # return " ".join(reversed(s.split())) # more concise; but slower in python3
    s = s.split()
    s.reverse()
    return " ".join(s)

if __name__=="__main__":
  sol = Solution()
  print(sol.reverseWords("the sky is blue")) # => "blue is sky the"
