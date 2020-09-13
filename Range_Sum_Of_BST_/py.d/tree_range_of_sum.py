from typing import List

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
  def __init__(self, val):
    self.node = val
    self.left = None
    self.right = None

  def insert_node(self, tree_node, location=None):
      print(location)
      if not location:
        print(f"found no value - inserting {val}")
        #print("\n")
        location = tree_node
      else:
        if tree_node.node > location.node:
          print(f"{tree_node.node} is > {location.node} - going right")
          self.insert_node(val, location.right)
        else:
          print(f"{tree_node.node} is < {location.node} - going left")
          self.insert_node(val, location.left)

  def ascend_tree(self, node=None):
    if node == None:
      node = self
    if node:
      self.ascend_tree(node.left)
      print(node.node)
      self.ascend_tree(node.right)

class Solution:
  def __init__(self):
    pass

  def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    return(root.val, root.left.left.left.val, root.left.right.left.val)

if __name__=="__main__":
  sol = Solution()
  # [10,5,15,3,7,13,18,1,None,6], L=7, R=15 => 45

  # manual btree definition
  # define root left
  '''
  ll = TreeNode(val=3, left=TreeNode(val=1))
  lr = TreeNode(val=7, left=TreeNode(val=6))
  l = TreeNode(val=5, left=ll, right=lr)

  # define root right
  rl = TreeNode(val=13)
  rr = TreeNode(val=18)
  r = TreeNode(val=15, left=rl, right=rr)

  # define root
  root = TreeNode(val=10, left=l, right=r)
  '''
  tree_vals = [10,5,15,3,7,13,18,1,None,6]
  tree_vals = [val for val in tree_vals if type(val) == int]
  new_tree = TreeNode(tree_vals.pop(0))
  #print(new_tree)
  for val in tree_vals:
    new_tree.insert_node(TreeNode(val), location=new_tree)
  '''
  iter_vals = map(lambda x: new_tree.insert_node(x), tree_vals)
  while True:
    try:
      next(iter_vals)
    except StopIteration:
      break
  '''
  #print(new_tree.node, new_tree.left, new_tree.right)
  #new_tree.ascend_tree()
