#include <unordered_map>
#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <set>
using namespace std;

class Solution{
  public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums){
      vector<int> nums_sorted (nums.begin(), nums.end());
      vector<int> nums_smaller;
      unordered_map<int, int> index_map; 
      unordered_map<int, int>::iterator found;  
      int tmp;
      int counter=0;

      for (int i=0; i < nums_sorted.size()-1; i++){
        for (int j=(i+1); j < nums_sorted.size(); j++){
          if (nums_sorted[i] > nums_sorted[j]){
            tmp = nums_sorted[i];
            nums_sorted[i] = nums_sorted[j];
            nums_sorted[j] = tmp; 
          }
        }
      }
      for (auto n: nums){
        found = index_map.find(n);
        if (found == index_map.end()){
          while (nums_sorted[counter] != n){
            counter+=1;
          }
          index_map.insert({n, counter});
          counter = 0;
          found = index_map.find(n);
        }
        nums_smaller.push_back(found->second);
      } 
      return nums_smaller;
    }
};



int main(){
  vector<int> nums = {16,4,2,47,2,8,1,1,5,3};
  Solution sol;
  sol.smallerNumbersThanCurrent(nums);
  return 0;
}
