from typing import List
from collections import deque

# [10,5,15,3,7,13,18,1,null,6] => becomes
# L=7, R=15 => 45
'''
                   10
                 /    \
                5     15
              /   \  /   \
             3    7 13   18
           /     /
          1     6
'''
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = None
    self.right = None

  def insert_node(self, val, location=None):
    '''
    Working constructor function for LeetCode b-tree questions
    (where b-tree is stated as list of ints and null values)
    '''
    if not location:
      location = TreeNode(val)
    else:
      if val > location.val:
        # we go right
        if not location.right:
          location.right = TreeNode(val)
        else:
          self.insert_node(val, location=location.right)
      elif val < location.val:
        # we go left
        if not location.left:
          location.left = TreeNode(val)
        else:
          self.insert_node(val, location=location.left)

  @classmethod
  def ascend_tree(cls, node=None):
    if node:
      cls.ascend_tree(node.left)
      print(node.val)
      cls.ascend_tree(node.right)

class Solution:
  def __init__(self):
    self.range_nodes = []

  def seek_nodes_in_range(self, L, R, node=None):
    if node:
      if node.val > L: self.seek_nodes_in_range(L, R, node.left)
      if node.val >= L and node.val <= R:
        #print(f'Node {node.val} would be appended')
        self.range_nodes.append(node.val)
      if node.val < R: self.seek_nodes_in_range(L, R, node.right)

  def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    self.seek_nodes_in_range(L, R, root)
    return sum(self.range_nodes)

if __name__=="__main__":
  sol = Solution()
  # [10,5,15,3,7,13,18,1,None,6], L=7, R=15 => 45
  tree_vals = [10,5,15,3,7,13,18,1,None,6]
  left, right = (7, 15)

  tree_vals = deque([val for val in tree_vals if type(val) == int])
  new_tree = TreeNode(tree_vals.popleft())

  # insert all nodes into new_tree
  while tree_vals:
    new_tree.insert_node(tree_vals.popleft(), location=new_tree)

  # ascend tree and display node values
  TreeNode.ascend_tree(node=new_tree) # => works

  print(sol.rangeSumBST(new_tree, left, right)) # should return 45
