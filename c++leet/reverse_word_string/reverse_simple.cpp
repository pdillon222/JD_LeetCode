#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
using namespace std;


class Solution{
  public:
    string reverseWords(string s){
      string reversed;
      bool blank_flag = true;
      int string_scan, substr_start, substr_end;
      size_t first_char, last_char;
      first_char = s.find_first_not_of(" ");

      if (first_char != string::npos){
        s.erase(0, first_char);

        // now that string has been resized
        // - find new index of final non-blank char

        last_char = s.find_last_not_of(" ");
        s.erase(last_char+1, s.length() - last_char);
        string_scan = substr_start = substr_end = s.length() - 1;

        // now the fun begins
        // - 
        while (string_scan > 0){
          if (s[string_scan] != ' ' && blank_flag){
            blank_flag = false;
            substr_end = string_scan; 
          } else if (s[string_scan] == ' ' && ! blank_flag){
            blank_flag = true;
            reversed += s.substr(string_scan + 1, substr_end - (string_scan));
            reversed += " ";
          } 
          string_scan--; 
        }

        substr_end = s.find_first_of(" ");
        if (substr_end != string::npos){
          reversed += s.substr(0, substr_end);
        } else {
          reversed += s.substr(0, s.length());
        }
      } else {
        // denotes a string of all " "'s
        reversed = ""; 
      }
      return reversed;
    };
};


int main(){
  Solution sol;
  string test_string;
  vector<string> test_strings = {
    "  a good  example  ",
    "the sky is blue",
    "  hello world!  ",
    "1 ",
    " ",
    "",
    "  ",
    "    ",
    "a"
  };

  for (auto x: test_strings){
    cout << "Testing string -> `" << x << "`" << endl;
    test_string = sol.reverseWords(x);
    cout << "String result == `" << test_string << "`" << "\n\n";
  }
  return 0;
}
