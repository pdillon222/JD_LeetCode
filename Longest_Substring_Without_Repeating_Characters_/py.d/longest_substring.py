class Solution:
    def lengthOfLongestSubstring(self, s: str, test_map: dict) -> int:
        return 3


if __name__=="__main__":
    sol = Solution()
    test_map = {
        "abcabcbb": 3,
        "bbbbb": 1,
        "pwwkew": 3
    }
    print(list(map(lambda _str: sol.lengthOfLongestSubstring(_str, test_map) == test_map[_str], test_map.keys())))
