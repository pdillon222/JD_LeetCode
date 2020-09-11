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
    self.left = left
    self.right = right

class Solution:
  def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    return(root.val, root.left.left.left.val, root.left.right.left.val)

if __name__=="__main__":
  sol = Solution()
  # [10,5,15,3,7,13,18,1,null,6], L=7, R=15 => 45

  # define root left
  ll = TreeNode(val=3, left=TreeNode(val=1))
  lr = TreeNode(val=7, left=TreeNode(val=6))
  l = TreeNode(val=5, left=ll, right=lr)

  # define root right
  rl = TreeNode(val=13)
  rr = TreeNode(val=18)
  r = TreeNode(val=15, left=rl, right=rr)

  # define root
  root = TreeNode(val=10, left=l, right=r)

  print(sol.rangeSumBST(root, 7, 15))
