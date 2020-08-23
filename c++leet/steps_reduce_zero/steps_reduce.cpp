#include <iostream>
#include <stdio.h>
using namespace std;

/*
Given a non-negative integer num, 
return the number of steps to reduce it to zero. 
If the current number is even, you have to divide it by 2, 
otherwise, you have to subtract 1 from it.
*/

class Solution{
  public:
    int numberOfSteps(int num);
};


int Solution::numberOfSteps(int num){
  int counter = 0;
  while (num > 1){
    if (num % 2 == 0){
      cout << num << " is divisible by 2" << endl;
      cout << "Dividing " << num << " by 2" << endl;
      num /= 2;
      cout << "New value of num " << num << endl;
      counter += 1;
    } else {
      cout << num << " is not divisible by 2" << endl;
      cout << "Reducing " << num << " by 1" << endl;
      num -= 1;
      cout << "New value of num " << num << endl;
      counter += 1; 
    }
  }
  cout << "Loop exiting: subtracting counter by 1" << endl;
  counter +=1;
  return counter;
}


int main(){
  Solution solution;
  int num_steps = solution.numberOfSteps(5);
  cout << "\n\n" << num_steps << "\n";
  return 0;
}
