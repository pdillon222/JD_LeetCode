class SubrectangleQueries:
  def __init__(self, rectangle: list):
    self.rectangle = rectangle


  def updateSubrectangle(self, row1: int,
                               col1: int,
                               row2: int,
                               col2: int,
                               newValue: int) -> None:
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
