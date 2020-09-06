/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var selfDividingNumbers = function(left, right) {
  let divisible_nums = [];
  for (; left <= right; left++){
    let self_divisible = true;
    left.toString().split("").map(num => {
      if (num === 0 || left % num != 0){
        self_divisible = false;
      }
    });
    if (self_divisible === true) divisible_nums.push(left);
  }
  return divisible_nums;
};


console.log(selfDividingNumbers(1, 22)); // => [1,2,3,4,5,6,7,8,9,11,12,15,22]
