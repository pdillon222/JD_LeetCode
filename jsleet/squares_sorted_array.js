#!/usr/bin/node

/**
Given an array of integers A sorted in non-decreasing order, 
return an array of the squares of each number, 
also in sorted non-decreasing order.

 * @param {number[]} A
 * @return {number[]}
 */
var sortedSquares = function(A) {
  A = A.map(num => num**2);
  return A.sort((a,b) => a - b);
}
