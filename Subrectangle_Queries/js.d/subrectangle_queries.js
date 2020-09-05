
/**
 * @param {number[][]} rectangle
 */
var SubrectangleQueries = function(rectangle) {
  this.rectangle = rectangle;
};


SubrectangleQueries.prototype.updateSubrectangle = function(row1, col1, row2, col2, newValue) {
  // Optimized:
  /*
  for (let i = row1; i <= row2; i++) {
    for (let j = col1; j <= col2; j++) {
      this.rectangle[i][j] = newValue
    }
  }
  */

  for (i=row1; i <= row2; i++){
    for (j=col1; j <= col2; j++){
      this.rectangle[i][j] = newValue;
    }
  }
};


SubrectangleQueries.prototype.getValue = function(row, col) {
  console.log(this.rectangle);
  return this.rectangle[row][col];
};

var rectangle = [[1,2,1],
                 [4,3,4],
                 [3,2,1],
                 [1,1,1]]


var new_rect = new SubrectangleQueries(rectangle);
new_rect.updateSubrectangle(0,0,3,2,5);
console.log(new_rect.getValue(1,2));
