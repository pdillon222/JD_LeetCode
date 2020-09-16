from typing import List
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#     self.val = val
#     self.left = left
#     self.right = right

# TODO - construct a method to build the tree from given list:
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

  def ascend_tree(self, node=None):
    if node == None:
      node = self
    if node:
      self.ascend_tree(node.left)
      print(node.val)
      self.ascend_tree(node.right)

class Solution:
  def __init__(self):
    pass

  def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    return(root.val, root.left.left.left.val, root.left.right.left.val)

if __name__=="__main__":
  sol = Solution()
  # [10,5,15,3,7,13,18,1,None,6], L=7, R=15 => 45
  tree_vals = [10,5,15,3,7,13,18,1,None,6]
  tree_vals = deque([val for val in tree_vals if type(val) == int])
  new_tree = TreeNode(tree_vals.popleft())

  while tree_vals:
    new_tree.insert_node(tree_vals.popleft(), location=new_tree)

  print("First Level:}")
  print(f'Node -> {new_tree.val}; Left -> {new_tree.left.val}; '
        f'Right -> {new_tree.right.val}')
  print("\nSecond Level left:")
  print(f'Node -> {new_tree.left.val}; Left -> {new_tree.left.left.val}; '
        f'Right -> {new_tree.left.right.val}')
  print("\nSecond Level right:")
  print(f'Node -> {new_tree.right.val}; Left -> {new_tree.right.left.val}; '
        f'Right -> {new_tree.right.right.val}')
