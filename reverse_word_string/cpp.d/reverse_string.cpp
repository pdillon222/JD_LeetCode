#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
using namespace std;

class Solution{
  public:
    string reverseWords(string s);
    string strip_blank_ends(string s);
    string vector_join_string(vector<string> str_vec); 
};


string Solution::strip_blank_ends(string s){
  int starter = 0;
  int str_len = s.length();
  while (s[starter] == ' ' and starter < str_len){
    s.erase(starter, 1);
    str_len = s.length();
  }
  starter = s.length() - 1;
  while(s[starter] == ' ' and starter >= 0){
    s.erase(starter, 1);
    starter = s.length() - 1;
  } 
  return s;
}


string Solution::vector_join_string(vector<string> str_vec){
  string from_vector;
  for (int i=0; i < str_vec.size(); i++){
    from_vector += str_vec[i];
    if (i != str_vec.size() - 1) from_vector += " ";
  }
  return from_vector;
}


string Solution::reverseWords(string s){
  string reversed;
  vector<string> substr_collect;
  s = this->strip_blank_ends(s);
  bool start_flag,end_flag = true;
  int end_substr = s.length()-1;
  int start_substr = 0;

  for (int i=0; i < s.length(); i++){
    if (s[i] != ' '){
      if (! start_flag){
        start_flag = true;
        end_flag = false;
        start_substr = i;
      }
    } else {
      if (! end_flag){
        end_flag = true;
        start_flag = false;
        end_substr = i;
        reversed = s.substr(start_substr, end_substr-start_substr);
        substr_collect.insert(substr_collect.begin(), reversed);
      }
    }
  }
  reversed = s.substr(start_substr, s.length() - start_substr);
  substr_collect.insert(substr_collect.begin(), reversed);
  //for (auto x: substr_collect) cout << x << endl;
  s = this->vector_join_string(substr_collect);
  cout << s << endl;
  return s;
}


int main(){
  Solution sol;
  //string test_string = "  a good  example  ";
  string test_string = "the sky is blue";
  sol.reverseWords(test_string); 
  return 0;
}
