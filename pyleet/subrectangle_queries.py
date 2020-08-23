#!/usr/bin/python3.7

"""
Implement the class SubrectangleQueries which receives 
a rows x cols rectangle as a matrix of integers in the 
constructor and supports two methods:
 - 1. updateSubrectangle(int row1, 
                         int col1, 
                         int row2, 
                         int col2, 
                         int newValue)
      - Updates all values with newValue in the 
        subrectangle whose upper left coordinate 
        is (row1,col1) and bottom right coordinate 
        is (row2,col2).

  - 2. getValue(int row, int col)
       - Returns the current value of the coordinate 
         (row,col) from the rectangle.
"""
class SubrectangleQueries:
  def __init__(self, rectangle: list):
    self.rectangle = rectangle
      

  def updateSubrectangle(self, row1: int, 
                               col1: int, 
                               row2: int, 
                               col2: int, 
                               newValue: int) -> None:
    """updateSubrectangle

    Updates the subrectangle belonging to self.rectangle
    whose upper left coordinate is (row1,col1) and bottom
    left coordinate is (row2,col2)

    Args:
      row1: 
      col1:
      row2:
      col2:
      newValue: 
     
    Returns:
      None 
    """
    if (row1, col1) == (row2, col2): 
      self.rectangle[row1][col1] = newValue
    else: 
      for row in range(row1, row2 +1):
        self.rectangle[row] = self.rectangle[row][:col1] + \
                              [newValue for column in range(col1, col2+1)] + \
                              self.rectangle[row][col2+1:]


  def getValue(self, row: int, col: int) -> int:
    return self.rectangle[row][col]


if __name__== "__main__":
  rectangle = [[1,2,1],
               [4,3,4],
               [3,2,1],
               [1,1,1]]

  obj = SubrectangleQueries(rectangle)
  obj.updateSubrectangle(0,0,3,2,5)
  print(obj.rectangle) 
