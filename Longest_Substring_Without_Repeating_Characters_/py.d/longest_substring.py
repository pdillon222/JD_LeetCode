
from test_assertions import map_cases

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return len(s)


if __name__=="__main__":
    sol = Solution()
    test_map = {
        "abcabcbb": 3,
        "bbbbb": 1,
        "pwwkew": 3
    }

    map_cases(test_map, sol.lengthOfLongestSubstring)
