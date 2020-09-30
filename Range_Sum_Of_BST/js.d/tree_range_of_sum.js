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
  insertNode (val, location){
    //location = (location===undefined ? null : location)
    if (val){
      if (!location){
        console.log(`Inserting node value == ${val}\n`)
        location = new TreeNode(val);
      } else {
        if (val < location.val){
          // go left
          if (! location.left){
            location.left = new TreeNode(val);
          } else {
            console.log(`${val} < ${location.val}: going left`)
            this.insertNode(val, location.left)
          }
        } else {
          // go right
          if (! location.right){
            location.right = new TreeNode(val);
          } else {
            console.log(`${val} > ${location.val}: going right`)
            this.insertNode(val, location.right)
          }
        }
      }
    }
  }
};

/** LeetCode function - passing in constructed BST
 * @param {TreeNode} root
 * @param {number} L
 * @param {number} R
 * @return {number}
 */
var rangeSumBST = function(root, L, R) {
  let stack = [root];
  let rangeNodes = [];
  let findNodesInRange = (node) => {
    if (node && node.val >= L && node.val <= R) rangeNodes.push(node.val);
    if (node.left && node.val >= node.left.val) stack.push(node.left);
    if (node.right && node.val <= node.right.val) stack.push(node.right);
  };
  while (stack.length > 0){
    findNodesInRange(stack.shift());
  }
  return rangeNodes.reduce((a,b) => a+b, 0);
};


let nodeVals = [10,5,15,3,7,13,18,1,null,6];
var tn = new TreeNode(nodeVals.shift())
nodeVals.map(n => tn.insertNode(n, tn));

console.log(rangeSumBST(tn, 7, 15));
