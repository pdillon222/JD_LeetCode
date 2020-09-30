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
    ////
    /* Private recursive node insert function,
       called by public TreeNode initializer `insertNode`
    */
    void insert(TreeNode *&nodePtr, TreeNode *&newNode){
      if (nodePtr == nullptr)
        nodePtr = newNode;                     // Insert the node
      else if (newNode->val < nodePtr->val)
        insert(nodePtr->left, newNode);        // Search the left branch
      else
        insert(nodePtr->right, newNode);       // Search the right branch
    }
    ////
    TreeNode *root;                            // Pointer to the root node
  public:
    ////
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
    ////
    ////
    TreeNode copyRoot(){
      return *this->root;
    }
    ////
    ////
    void ascendTree(TreeNode *nodeptr){
      if (nodeptr){
        ascendTree(nodeptr->left);
        printf("%d\n", nodeptr->val);
        ascendTree(nodeptr->right);
      }
    }
    ////
    /*
    - Functions above are merely for TreeNode construction and description
      Leetcode solution functions are below:
    */
    ////
    void nodesInRange(TreeNode *nodeptr, vector<int> &nodeRange, int L, int R){
      if (nodeptr){
         if (nodeptr->val >= L && nodeptr->val <= R){
           printf("Pushing back %d\n", nodeptr->val);
           nodeRange.push_back(nodeptr->val);
         }
         if (nodeptr->val > L)
           nodesInRange(nodeptr->left, nodeRange, L, R);
         if (nodeptr->val < R)
           nodesInRange(nodeptr->right, nodeRange, L, R);
      }
    }
    ////
    ////
    int rangeSumBST(TreeNode* root, int L, int R) {
      vector<int> nodeRange;
      int nodeSum = 0;
      nodesInRange(root, nodeRange, L, R);
      for (auto node: nodeRange)
        nodeSum += node;
      return nodeSum;
    }
    ////
};


int main(){
  int left, right;
  left = 7;
  right = 15;
  vector<int> node_vals = {10,5,15,3,7,13,18,1,6};

  Solution *sol = new Solution;
  for (auto val: node_vals)
    sol->insertNode(val);

  //copy new TreeNode from sol object to struct outside of class
  TreeNode *newNode = new TreeNode;
  *newNode = sol->copyRoot();
  //display tree structure in ascending value order
  sol->ascendTree(newNode);
  cout << endl;
  //sol->ascendTree();

  sol->rangeSumBST(newNode, left, right);
  delete sol;
  delete newNode;
  return 0;
}


/* Optimized solution:
static auto speedup = [](){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    return nullptr;
}();


class Solution {
public:
    int rangeSumBST(TreeNode* root, int L, int R) {
        if (root == NULL)
            return 0;
        int x=rangeSumBST(root->left,L,R);
        int y=rangeSumBST(root->right,L,R);
        if(root->val>=L && root->val<=R)
                return (root->val + x + y);
        else
            return x+y;
    }
};
*/
