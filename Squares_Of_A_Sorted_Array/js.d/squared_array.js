var sortedSquares = function(A) {
  A = A.map(num => num**2);
  return A.sort((a,b) => a - b);
}

console.log(sortedSquares([-4,-1,0,3,10])); // => [0,1,9,16,100]
