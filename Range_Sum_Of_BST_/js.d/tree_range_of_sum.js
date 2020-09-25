// [10,5,15,3,7,13,18,1,null,6] => becomes
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
// LeetCode definition for a binary tree node.
/*
function TreeNode(val, left, right) {
  this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
  this.right = (right===undefined ? null : right)
}
*/

// ES6 implementation
class TreeNode {
  constructor (val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
  }
  // Node insertion function
  insertNode (newNode, location){
    location = (location===undefined ? null : location)
    if (!location){
      location = newNode;
    } else {
      if (newNode.val < location.val){
        // go left
        this.insertNode(newNode, location.left)
      } else {
        // go right
        this.insertNode(newNode, location.right)
      }
    }
  }

  // External treenode generator function
  newNode (val) {
    // construct a new TreeNode from val
    newNode = new TreeNode(val)
    this.insertNode(newNode)
  }
}

/** LeetCode function - passing in constructed BST
 * @param {TreeNode} root
 * @param {number} L
 * @param {number} R
 * @return {number}
 */
var rangeSumBST = function(root, L, R) {
    console.log(root);
    root.insertNode(5);
    console.log(root);
};

var tn = new TreeNode(4);
rangeSumBST(tn, 7, 15);
