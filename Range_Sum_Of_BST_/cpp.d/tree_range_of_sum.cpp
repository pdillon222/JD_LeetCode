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
// Definition for a binary tree node
struct TreeNode
{
  int val;         // Holds the integer val in node
  TreeNode *left;    // Pointer to the left child node
  TreeNode *right;   // Pointer to the right child node
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
  private:
    // Private recursive node insert function,
    // called by public TreeNode initializer `insertNode`
    void insert(TreeNode *&nodePtr, TreeNode *&newNode){
      if (nodePtr == nullptr)
        nodePtr = newNode;                     // Insert the node
      else if (newNode->val < nodePtr->val)
        insert(nodePtr->left, newNode);        // Search the left branch
      else
        insert(nodePtr->right, newNode);       // Search the right branch
    }

  public:
    TreeNode *root;      // Pointer to the root node
    // public interface to emplace nodes into root TreeNode
    void insertNode(int num, TreeNode *nodePtr=nullptr){
      TreeNode *newNode = nullptr;
      // Create a new node and store num in it
      newNode = new TreeNode;
      newNode->val = num;
      newNode->left = newNode->right = nullptr;
      // if no arg for nodePtr: use object TreeNode root
      // TODO - how to execute below as ternary oneliner
      if (nodePtr == nullptr){
        printf("Inserting %d into object TreeNode root\n", num);
        insert(root, newNode);
      } else {
        printf("Inserting %d into TreeNode obj at mem address -> %p\n", num, &nodePtr);
        insert(nodePtr, newNode);
      }
    }
    int rangeSumBST(TreeNode* root, int L, int R) {

      return 0;
    }
};


// TODO -
/*
   - Create ascendTree function
   - Make root private
   - create public copy constructor (copies obj.root to TreeNode
       instantiated outside of class)
*/


int main(){
  int left, right;
  left = 7;
  right = 15;
  vector<int> node_vals = {10,5,15,3,7,13,18,1,6};

  Solution *sol = new Solution;
  for (auto val: node_vals)
    sol->insertNode(val);

  //display tree structure in ascending value order
  //sol->ascendTree();

  //sol->rangeSumBST(sol->root, left, right);
  delete sol;
  return 0;
}
