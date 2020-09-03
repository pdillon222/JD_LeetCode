#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;


class Solution {
  public:
    vector<int> decompressRLElist(vector<int>& nums);
};


vector<int> Solution::decompressRLElist(vector<int>& nums){
  vector<int> dcmprsd_nums;
  for (int i=0; i < nums.size() - 1; i+= 2){
    for (int j=0; j < nums[i]; j++){
      dcmprsd_nums.push_back(nums[i+1]);
    }
  }
  for (auto x: dcmprsd_nums)
    cout << x << " ";
  cout << endl;
  return dcmprsd_nums;
}


int main(){
  Solution sol;
  vector<int> nums = {1,1,2,3};
  sol.decompressRLElist(nums);
  return 0;
}
