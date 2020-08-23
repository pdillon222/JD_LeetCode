#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <regex>
using namespace std;

class Solution{
  public:
    string reverseWords(string s){
      vector<int> blank_indices;
      string reversed;
      string strip_start_end = "^ *| *$";
      string mid_strip = " {2,}";
      regex strip_tails(strip_start_end);
      regex strip_mid(mid_strip);
      string blank = "";
      string space = " ";
      s = regex_replace(s, strip_tails, blank);
      s = regex_replace(s, strip_mid, space);

      // parse the string for all occurrences of " ", add index to blank_indices
      size_t blank_index = s.find(space);
      size_t position;
      while (blank_index != string::npos){
        if (blank_index != string::npos){
          position = blank_index;
          blank_indices.push_back(position);
        }
        blank_index = s.find(space, position+1); 
      }
      if (blank_indices.size() == 0)
        return s;

      string substring;
      int blank_diff;
      for (int i=blank_indices.size()-1; i>-1;i--){
        //cout << blank_indices[i] << endl;
        if (i == blank_indices.size()-1){
          //cout << "substring to add == " << "_" << s.substr(blank_indices[i]+1, s.length() - blank_indices[i]+1) << "_" << endl;
          reversed += s.substr(blank_indices[i]+1, s.length() - blank_indices[i]);
        } else {
          blank_diff = blank_indices[i+1] - blank_indices[i]-1;
          //cout << "blank diff == " << blank_diff << endl;
          //cout << "substring to add == _" << s.substr(blank_indices[i]+1, blank_diff) << "_" << endl;
          reversed += s.substr(blank_indices[i]+1, blank_diff);
        } 
        reversed += " ";
      } 
      //cout << "end of loop" << endl;
      //cout << "substring to add == " << "_" << s.substr(0, blank_indices[0]) << "_" << endl;
      reversed += s.substr(0, blank_indices[0]);
      return reversed;
    };
};


int main(){
  Solution sol;
  string test_string;
  vector<string> test_strings = {
    "  a good  example  ",
    "the sky is blue",
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
  sol.reverseWords(test_string); 
  return 0;
}
