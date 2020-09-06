#include <iostream>
#include <vector>
#include <stdio.h>
using namespace std;


class Solution {
private:
  bool div_zero_flag;
  void divisible_int(int sub_num, int num){
    if (sub_num >= 10 and this->div_zero_flag)
      divisible_int(sub_num / 10, num);
    sub_num = sub_num % 10;
    cout << "Testing divisibility of " << num << "/" << sub_num << endl;
    if (sub_num != 0 && num % sub_num == 0){
      cout << num << " is divisible by " << sub_num << endl;
    } else {
      cout << num << " is not divisible by " << sub_num << "!!!" << endl;
      this->div_zero_flag = false;
    }
    cout << endl;
  }

public:
  vector<int> selfDividingNumbers(int left, int right){
    vector<int> self_divide;
    for (;left <= right; left++){
      this->div_zero_flag = true;
      this->divisible_int(left, left);
      if (this->div_zero_flag){
        cout << left << " is self divisible; appending" << endl;
        self_divide.push_back(left);
      }
      cout << "Done iterating for " << left << endl << endl;
    }

    return self_divide;
  }
};


int main(){
  int left = 1, right = 22; // => => [1,2,3,4,5,6,7,8,9,11,12,15,22]
  Solution sol;
  vector<int> nums = sol.selfDividingNumbers(left, right);
  for (auto x: nums)
    cout << x << " ";
  cout << endl;
  return 0;
}
