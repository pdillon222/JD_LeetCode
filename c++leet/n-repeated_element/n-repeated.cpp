#include <iostream>
#include <stdio.h>
#include <unordered_map>
#include <vector>
using namespace std;

//g++ -std=c++11 n-repeated.cpp -o nout
/*
In a array A of size 2N, there are N+1 unique elements, 
and exactly one of these elements is repeated N times.
Return the element repeated N times
*/

class Solution{
  public:
    int repeatedNTimes(vector<int>& A);
};

int Solution::repeatedNTimes(vector<int>& A)
{
  int key;
  unordered_map<int, int> num_counts;
  unordered_map<int, int>::const_iterator found;  

  for (auto i: A)
  {
    found = num_counts.find(i);
    if (found == num_counts.end())
    {
      //cout << i << " not found in unordered_map; inserting" << endl;
      num_counts.insert({i,1});
    } else {
      //cout << i << " is in unordered_map; incrementing" << endl;
      //cout << num_counts[i] << endl;
      num_counts[i] += 1;
      if (A.size()/2 == num_counts[i])
        return i;
    }
  }
  
  return 0;
}

int main()
{
  vector<int> nums = {5,1,5,2,5,3,5,4}; //This should return 5
  Solution instance;
  int val = instance.repeatedNTimes(nums);
  cout << "\n\n" << val << endl;
  return 0;
}
