#include <iostream>
#include <string>
#include <vector>
#include <stdio.h>
using namespace std;


class Solution{
  public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies);
};


vector<bool> Solution::kidsWithCandies(vector<int>& candies, int extraCandies){
  vector<bool> most_candies = {};
  int largest_num = 0;
  for (auto x: candies){
    if (x > largest_num)
      largest_num = x;
  }
  for (auto x: candies){
    if (x + extraCandies >= largest_num){
      most_candies.push_back(true);
    } else {
      most_candies.push_back(false);
    }
  }
  return most_candies;
}


int main(){
  vector<int> candies = {4,2,1,1,2};
  Solution sol;
  vector<bool> hasMost = sol.kidsWithCandies(candies, 1);
  for (auto x: hasMost)
    cout << x << " ";
  cout << endl;
  return 0;
}
