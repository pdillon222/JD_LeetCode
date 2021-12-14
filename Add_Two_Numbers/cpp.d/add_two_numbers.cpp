#include <iostream>
#include <stdio.h>
#include <vector>
#include <math.h>

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
	  void insert(ListNode** root, int item){
	      ListNode* temp = new ListNode;                                   // initialize New ListNode, incase root is empty
	      ListNode* ptr;                                                   // initialize ListNode to be traversed ?
	      temp->val = item;
	      temp->next = NULL;

	      if (*root == NULL){
			      *root = temp;                                               // if value of root is empty
	      } else {
			      ptr = *root;
			      while (ptr->next != NULL)
					      ptr = ptr->next;
			      ptr->next = temp;
	      }
        cout << item << " successfully placed in linked list" << endl;
    }

	  ListNode* initFromVector(vector<int>& vec){
        ListNode* newNode = NULL;
        for (auto x: vec){
            cout << "Placing " << x << " in linked list" << endl;
            this->insert(&newNode, x);
        }
        cout << endl;
			  return newNode;
	  }

    ListNode* initFromArray(int arr[], int n){
      ListNode *root = NULL;
			for (int i = 0; i < n; i++) {
          cout << "Placing " << arr[i] << " in linked list" << endl;
          this->insert(&root, arr[i]);
      }
      cout << endl;
      return root;
    }

    void traverseList(ListNode* root){
        while (root != NULL){
            cout << root->val << " -> ";
            root = root->next;
        }
        cout << endl;
    }
    /*
    long long intReverse(ListNode* root){
        long long power = 0, sum = 0;
        ListNode* temp = root;
        while (temp != NULL){
            sum += temp->val * (pow(10, power));
            cout << "New sum val => " << sum << endl;
            temp = temp->next;
            power += 1;
        }
        cout << "sum = " << sum << endl;
        return sum;
    }
    */
		long double intReverse(ListNode* root){
        // debug for issue w/ vector -> {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1}

        long double power = 0, sum = 0;
        long double adder = 0;
        ListNode* temp = root;
        while (temp != NULL){
            adder = temp->val * (pow(10, power));
            sum = sum + adder;
            cout << "New sum val => " << sum << "; pow val => " << power << "; adder val => " << adder << endl;
            temp = temp->next;
            power += 1;
        }
        cout << "sum = " << sum << endl;
        return sum;
    }

		ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        long double sum = this->intReverse(l1) + this->intReverse(l2);
        cout << "composite sum -> " << sum << " reversing" << endl;
        long double remainder = 0;
        ListNode* newNode = NULL;
        /*
        while (sum != 0){
            remainder = sum % 10;
            cout << "remainder val -> " << remainder << endl;
            sum /= 10;
            cout << "sum val -> " << sum << endl;
            this->insert(&newNode, remainder);
        }
        */
				return newNode;
		}
};


int main(){
    Solution sol;
    vector<int> v1 = {1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1};//{2, 4, 3};
    vector<int> v2 = {5, 6, 4};

    /*
    TODO - refactor -> int reverse to return reversed linked list instead of
    */

    ListNode* ll1 = sol.initFromVector(v1);
    ListNode* ll2 = sol.initFromVector(v2);
    ListNode* revSum = sol.addTwoNumbers(ll1, ll2);
    return 0;
}
