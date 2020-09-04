/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function(candies, extraCandies) {
  const maxCandy = Math.max(...candies);
  var hasMost = [];
  candies.map(candy => {hasMost.push(candy + extraCandies >= maxCandy)});
  return hasMost;
};

console.log(kidsWithCandies([2,3,5,1,3], 3)) // => [true,true,true,false,true]
