#include<iostream>
#include<vector>
#include<stdio.h>

using namespace std;

// {10,5,15,3,7,13,18,1,null,6} => becomes
// L=7, R=15 => 45
/*
                   10
                 /    \
                5     15
              /   \  /   \
             3    7 13   18
           /     /
          1     6
*/
// Definition for a binary tree node:
struct TreeNode {
   int val;
   TreeNode *left;
   TreeNode *right;
   TreeNode() : val(0), left(nullptr), right(nullptr) {}
   TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
   TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
   // Recursive function will build tree from node values
   void tree_builder(int val, TreeNode *&location){
     TreeNode *new_node = nullptr;
     new_node = new TreeNode;
     new_node->val = val;
     if (location == nullptr){
       cout << "emplacing TreeNode w/ value " << val << endl;
       location = &new_node;
       cout << location->val << endl;
       //location = TreeNode(val);
       //cout << location->val << " " << location->left << " " << location->right << endl;
       //cout << location->val << endl;
       //cout << location->val << endl;
     } else if (val > location->val){
         cout << val << " is > than " << location->val << "; Going right" << endl;
         tree_builder(val, location=location->right);
     } else {
         cout << val << " is < than " << location->right << "; Going left" << endl;
         tree_builder(val, location=location->left);
     }
   }
};


class Solution {
  public:
    int rangeSumBST(TreeNode* root, int L, int R) {
      cout << root->val << endl;
      cout << root->right << endl;
      cout << root->left << endl;
      return 0;
    }
};


int main(){
  int left, right;
  left = 7;
  right = 15;
  vector<int> node_vals = {10,5,15,3,7,13,18,1,6};

  // using default constructor
  TreeNode *new_tree = new TreeNode();

  // initializing val w/ int
  //TreeNode *new_tree = new TreeNode(5);

  // initializing val w/ int, and L&R w/ TreeNode pointers
  /*
  TreeNode *left_branch = new TreeNode();
  TreeNode *right_branch = new TreeNode();
  TreeNode *new_tree = new TreeNode(10, left_branch, right_branch);
  */

  Solution *sol = new Solution;
  for (auto val: node_vals)
    new_tree->tree_builder(val, new_tree);
  //sol->rangeSumBST(new_tree, left, right);
  cout << new_tree->val << endl << endl;

  cout << new_tree->right->val << " " << new_tree->left->val << endl;
  delete sol;
  delete new_tree;
  return 0;
}
