
/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps  = function(num) {
  let counter = 0;
  while (num > 1){
    if (num % 2 == 0){
      num /= 2;
      counter += 1;
    } else {
      num -= 1;
      counter += 1;
    }
  }
  counter +=1;
  return counter;
};

console.log(numberOfSteps(123)) // => 12
