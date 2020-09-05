var sortedSquares = function(A) {
  A = A.map(num => num**2);
  return A.sort((a,b) => a - b);
}
