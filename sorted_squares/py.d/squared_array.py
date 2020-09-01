#!/usr/local/bin/python3

import profile
import sys
import os

'''
for an arbitrary array of ints:
  [-5, -4, -3, -2, 1, 4, 6, 8]
Return an array containing the square of
each element in non-descending order
'''

'''
Interview question:
- Pretend I have a simple python script, wherein a user must pass in
  a list as the script's only argument.
- The script must understand the argument as a list: what is the initial
  problem?
- Define a way to define that string, representing a list as an actual
  list data type without calling eval:
- Can you do it as a list comprehension?
'''



def square_non_descending(array):
  #squares_dict = {key:val**2 for key,val in zip(array, [num**2 for num in array])}
  return sorted([num**2 for num in array])
  

if __name__=="__main__":
  array = [int(item.replace("[","").replace("]","").replace(" ","")) 
           for item in sys.argv[1].split(",")]
  profile.run('print(square_non_descending(array))')
