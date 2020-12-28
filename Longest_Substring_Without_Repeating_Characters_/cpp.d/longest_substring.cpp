#include <vector>
#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <unordered_map>


typedef std::unordered_map<std::string, int> expected_result;

class LongestSubstring {
public:
    int lengthOfLongestSubstring(std::string s){
        std::array <int, 256> last_index;
        last_index.fill(-1);
        int n = s.length();
        int max_substr_len = 0;
        int i = 0;

        for (int j=0; j<n; j++){
            i = std::max(i, last_index[(int)(s[j])] + 1);
            max_substr_len = std::max(max_substr_len, j - i + 1);
            last_index[(int)(s[j])] = j;
        }
        return max_substr_len;
    }

    bool function_validate(std::string s, int res){
      printf("Checking string -> %s\n", s.c_str());
      bool bool_result = this->lengthOfLongestSubstring(s) == res;
      if (bool_result){
        std::cout << "string " <<
        s << " yields correct result -> " <<
        res << "\n\n" ;
      } else {
        std::cout << "bool result no likey\n\n";
      }
    return bool_result;
    }
};

int main(){
  LongestSubstring ls;
  expected_result results({
    {"abcabcbb", 3},
    {"bbbbb", 1},
    {"pwwkew", 3},
    {"abcdefg", 7},
    {"aab", 2},
    {"dvdf", 3}
  });
  for (auto x: results){
    ls.function_validate(x.first, x.second);
  }
  return 0;
}
