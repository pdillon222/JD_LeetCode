/**
 * @param {number[]} A
 * @return {number}
 */
var repeatedNTimes = function(A) {
    counts = {};
    counts[A[0]] = 0;
    for (i=0; i<A.length; i++){
        //hasownproperty instead of loop;[]
        if (counts.hasOwnProperty(A[i])){
          counts[A[i]] += 1;
        } else {
          counts[A[i]] = 1;
        }
        if (counts[A[i]] == A.length / 2)
          return A[i];
    }
};

console.log(repeatedNTimes([1,2,3,3])) // => 3
