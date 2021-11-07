#include <iostream>
#include <stdio.h>

using namespace std;

struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
	  ListNode* initFromArray(int arr[]){
			  cout << "Hello from initFromArray!" << endl;
			  ListNode *tester;
			  //ListNode(arr[0]);
			  return tester;
	  }

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        cout << "Hello from addTwoNumbers!" << endl;
        ListNode *sumList;
        return l1;
    }
};


int main(){
    Solution sol;
    int arr1[3] = {2, 4, 3};
    int arr2[3] = {5, 6, 4};
    ListNode* ll1 = sol.initFromArray(arr1);
    /*
    ListNode* ll2 = sol.initFromArray(arr2);
    ListNode* listSums = sol.addTwoNumbers(ll1, ll2);
    */
    return 0;
}
