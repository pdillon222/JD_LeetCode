#!/home/james/VirtualEnvs/jenv38/bin/python

import re
import cProfile
import argparse
from typing import List, Set, Tuple, Dict
from colorama import init, Fore, Back, Style
init(autoreset=True)

class Solution:
  @classmethod
  def reservationsFromFile(_file):
    '''
    - _file is a long string representing a list of lists -> [[\d,\d],[\d,\d]...]]
    - convert string to list of lists of ints
    '''
    with open('reservedSeats','r') as rs:
      reservations = [[int(seat.replace('[','').replace(']',''))
                      for seat in _lst.split('*')]
                      for _lst in re.sub(r'\[(\d*),(\d*)\]', r'[\1*\2]',
                      rs.read().rstrip()[1:-1]).split(',')]
    return reservations

  def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
    # create a dictionary instead
    reserved_rows = {}
    for reservation in reservedSeats:
      if reservation[0] not in reserved_rows:
        reserved_rows[reservation[0]] = [reservation[1]]
      else:
        reserved_rows[reservation[0]].append(reservation[1])

    # aggregate a counter for all non-reserved rows, max arrangements = 2 for each
    seat_combos = (n - len(reserved_rows)) * 2

    for row in reserved_rows:
      #'''
      row_bool = [_seat not in [seat[1]
                  for seat in reservedSeats
                  if seat[0] == row]
                  for _seat in range(2,10)]
      #'''
      #row_bool = [_seat not in reserved_rows[row]
      #            for _seat in range(2,10)]
      #'''
      color_bool = [Back.GREEN + str(rsrvd_seat)
                    if rsrvd_seat else Back.RED + str(rsrvd_seat)
                    for rsrvd_seat in row_bool]
      #'''
      print("[" + ", ".join(color_bool) + "]")
      # arrangments -> row_bool[0:4], [2:6], [4:8]
      print(all(row_bool[0:4]), all(row_bool[2:6]), all(row_bool[4:8]))
      print("\n")
      if all(row_bool[0:4]) and all(row_bool[4:8]):
        # max 4 group arrangements met - increment seat_combos by 2
        print(f'Row {list(reserved_rows).index(row)} meets max arrangements;'
              f'incrementing by 2')
        seat_combos += 2
      elif all(row_bool[0:4]) or all(row_bool[2:6]) or all(row_bool[4:8]):
         print(f'Row {list(reserved_rows).index(row)} meets arrangement req;'
               f'incrementing by 1')
         seat_combos += 1
    print(seat_combos)
    return seat_combos



if __name__=="__main__":
  parser = argparse.ArgumentParser()
  n = 3
  reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
  ### values above return -> 4 ###

  n = 4
  reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
  ### values above return -> 4 ###

  n = 2646
  reservedSeats = Solution.reservationsFromFile()
  ### answer is right -> 2084
  ### need to optimize for time -> currenty at 7228 ms

  n = 3
  reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
  ### values above return -> 4 ####

  func_args = (n, reservedSeats)
  solution = Solution()

  def profile_it():
    print("\n\nCode Profiling:\n")
    cProfile.runctx('g(x,y)',
                    {'x': n,
                     'y': reservedSeats,
                     'g': solution.maxNumberOfFamilies},{})
  parser.add_argument('--profile', action='store_true')
  args = parser.parse_args()
  if args.profile:
    profile_it()
  else:
    solution.maxNumberOfFamilies((*func_args))

#####
#####

''' Optimized solution
class Solution:
    def maxNumberOfFamilies(self, n, reserved):
        d = {}
        for i, j in reserved:
            if j == 1 or j == 10:
                continue
            if i not in d:
                d[i] = (1 << 12) - 1
            d[i] ^= 1 << j

        k = 2 * (n - len(d))

        seats = (1 << 4) - 1
        a = seats << 2
        b = seats << 4
        c = seats << 6
        for x in d.values():
            q = x & a == a
            w = x & b == b
            e = x & c == c
            if q or w or e:
                k += 1
                if q and e:
                    k += 1

        return k
'''
