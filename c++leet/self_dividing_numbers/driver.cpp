/*
A general test-bed, for C++ fun times
for c++11 compilation: g++ -std=c++11 your_file.cpp -o your_program
*/

#include <iostream>
#include <iomanip>
#include <memory>
#include <vector>
#include <string.h>
#include <stdio.h>
using namespace std;


class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
      bool div_zero_flag;
      vector<int> self_divide;
      for (;left <= right; left++){
        /*
         - split integer->right into individual integers (init as new vector)
         - init boolean, testing for 0 division
         - loop through integers in new vector
           - if right % int != 0
        */
        div_zero_flag = true;
         
        self_divide.push_back(left);
      }
 
      return self_divide; 
    }
};


int main(){
  int left = 1, right = 22;
  Solution sol;
  vector<int> nums = sol.selfDividingNumbers(left, right);
  /* 
  for (int i=0; i < nums.size(); i++){
    cout << nums[i] << endl;
  }*/

  vector<int> tester = {144,543,66,79,85,954};
  for (i = 0; i < tester.size(); i++){

  }
  
  return 0;
}


