#include <iostream>
#include <vector>
#include <math.h>
#include <stdio.h>
using namespace std;


class Solution {
public:
  vector<int> sortedSquares(vector<int>& A) {
    int smallest_index;
    for (int i=0; i < A.size(); i++){
      A[i] = pow(A[i], 2);
    }

    for (int i=0; i < A.size(); i++){
      smallest_index = i;
      for (int j=i+1; j < A.size(); j++){
        if (A[j] < A[smallest_index])
          smallest_index = j;
      }
      if (smallest_index != i)
        A = int_swap(A, i, smallest_index);
    }
  return A;
  }
private:
  vector<int> int_swap(vector<int>& vec, int first, int last)
  {
    int temp = vec[first];
    vec[first] = vec[last];
    vec[last] = temp;
    return vec;
  }
};


int main(){
  Solution sol;
  vector<int> test_vec = {-4,-1,0,3,10};
  for (auto x: sol.sortedSquares(test_vec))
    cout << x << " "; // => 0 1 9 16 100
  cout << endl;
  return 0;
}
