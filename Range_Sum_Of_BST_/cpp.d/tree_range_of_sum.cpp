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
};


class Solution {
  public:
    int rangeSumBST(TreeNode* root, int L, int R) {
      cout << root->val << endl;
      cout << root->right << endl;
      cout << root->left << endl;
    }
    TreeNode tree_builder(vector<int>){
      // construct bst from vector of ints
      TreeNode built_tree(5);
      cout << built_tree.val << endl;
      return built_tree;
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
  sol->tree_builder(node_vals);
  sol->rangeSumBST(new_tree, left, right);
  delete sol, new_tree;
  return 0;
}
