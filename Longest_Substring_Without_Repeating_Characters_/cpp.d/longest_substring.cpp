#include <vector>
#include <stdio.h>
#include <iostream>
#include <unordered_map>

/*
- colored output -> https://stackoverflow.com/questions/9158150/colored-output-in-c/9158263
*/

typedef std::unordered_map<std::string, int> expected_result;

class LongestSubstring {
public:
    int lengthOfLongestSubstring(std::string s){
        return 3;
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
