/**
 * @param {number[]} nums
 * @return {number[]}
 */
var decompressRLElist = function(nums) {
    var dcmprsd_nums = [];
    for (var i=0; i < nums.length - 1; i+=2){
        for (var j=0; j < nums[i]; j++){
            dcmprsd_nums.push(nums[i+1]);
        }
    }
    return dcmprsd_nums;
};

console.log(decompressRLElist([1, 1, 2, 3])); // => [1, 3, 3]
