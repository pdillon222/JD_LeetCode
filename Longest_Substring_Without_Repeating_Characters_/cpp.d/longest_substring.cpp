#include <iostream>
#include <stdio.h>
#include <vector>

using namespace std;

class LongestSubstring {
public:
    int lengthOfLongestSubstring(string s){
        printf("Hello string -> %s\n", s.c_str());
    }
};

int main(){
  LongestSubstring ls;
  string teststring = "new string";
  ls.lengthOfLongestSubstring(teststring);

  return 0;
}


/*
test_map = {
    "abcabcbb": 3,
    "bbbbb": 1,
    "pwwkew": 3,
    "abcdefg": 7,
    "aab": 2,
    "dvdf": 3
}
*/
