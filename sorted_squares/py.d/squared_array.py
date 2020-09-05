import profile
import sys
import os

def square_non_descending(array):
  #squares_dict = {key:val**2 for key,val in zip(array, [num**2 for num in array])}
  return sorted([num**2 for num in array])


if __name__=="__main__":
  array = [int(item.replace("[","").replace("]","").replace(" ",""))
           for item in sys.argv[1].split(",")]
  profile.run('print(square_non_descending(array))')
