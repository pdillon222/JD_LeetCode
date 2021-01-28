#include <string>
#include <stdio.h>
#include <iostream>


class Solution {
  private:
    void buildLowestNumString(std::string str, int n, std::string &res){
      // If there are 0 characters to remove from str:
      // - append everything to result
      if (n == 0) {
        res.append(str);
        return;
      }
      int len = str.length();
      // If there are more characters to remove than string length:
      // - append nothing to result
      if (len <= n) return;
      // Find the smallest character among first (n+1) characters of str
      int minIndex = 0;
      for (int i = 1; i<=n ; i++) if (str[i] < str[minIndex]) minIndex = i;
      // Append the smallest character to result
      res.push_back(str[minIndex]);
      // Substring starting from minIndex+1 to str.length() - 1.
      std::string new_str = str.substr(minIndex+1, len-minIndex);
      // Recurse for the above substring and n equals to n-minIndex
      this->buildLowestNumString(new_str, n-minIndex, res);
    }
  public:
    std::string removeKdigits(std::string num, int k) {
      std::string res = "";
      this->buildLowestNumString(num, k, res);
      while (res[0] == '0') res.erase(0,1);
      return (res == "") ? "0" : res;
    }
};


int main(){
  Solution sol;
  std::string str = "121198";
  int n = 2;
  std::cout << sol.removeKdigits(str, n) << std::endl;  //1118
  str = "10200";
  n = 1;
  std::cout << sol.removeKdigits(str, n) << std::endl;  //200
  str = "10";
  n = 2;
  std::cout << sol.removeKdigits(str, n) << std::endl; //0
  return 0;
}
