/**
 * @param {number[]} nums
 * @return {number[]}
 */
var smallerNumbersThanCurrent = function(nums) {
    var nums_sorted = [...nums];
    nums_sorted.sort((a, b) => a - b);
    var nums_smaller = [];
    var index_map = {};
    for (i=0; i < nums.length; i++){
      if (! index_map.hasOwnProperty(nums[i])){
        index_map[nums[i]] = nums_sorted.indexOf(nums[i]);
      }
      nums_smaller.push(index_map[nums[i]])
    }
    return nums_smaller;
};

console.log(smallerNumbersThanCurrent([5,0,10,0,10,6])) // => [2,0,4,0,4,3]
