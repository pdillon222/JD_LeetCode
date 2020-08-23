#!/home/james/VirtualEnvs/jenv4/bin/python

import sys

works = [[559,511],[932,618],[-623,-443],[431,91],[838,-127]]
doesnt_work = [[559,511],[932,618],[-623,-443],[431,91],[838,-127],[773,-917]]
# should return 4179 ; is returning 3454
test_vals = [[559,511],[932,618],[-623,-443],[431,91],[838,-127],[773,-917],[-500,-910],[830,-417],[-870,73],[-864,-600],[450,535],[-479,-370],[856,573],[-549,369],[529,-462],[-839,-856],[-515,-447],[652,197],[-83,345],[-69,423],[310,-737],[78,-201],[443,958],[-311,988],[-477,30],[-376,-153],[-272,451],[322,-125],[-114,-214],[495,33],[371,-533],[-393,-224],[-405,-633],[-693,297],[504,210],[-427,-231],[315,27],[991,322],[811,-746],[252,373],[-737,-867],[-137,130],[507,380],[100,-638],[-296,700],[341,671],[-944,982],[937,-440],[40,-929],[-334,60],[-722,-92],[-35,-852],[25,-495],[185,671],[149,-452]]


def minTimePoints(points):
  if type(points) == str: points = eval(points)

  # separate out the x and y coordinates
  point_vals = lambda num, points: [point[num] for point in points]
  numerator, denominator = point_vals(0, points), point_vals(1, points)

  '''  
  # get the absolute distance between each point
  int_diff = lambda nums: sum([abs(nums[n] - nums[n+1]) for n in range(len(nums)-1)])
  '''

  print_str = lambda value, nums_list: "[Info]: Values in {} list = {}\n".format(value, 
              ",".join(list(map(lambda x: str(x), nums_list))))

  print(print_str("numerator", numerator))
  print(print_str("denominaotr", denominator))

  '''  
  # sort the x any y coordinate differences
  diff_list = sorted([int_diff(numerator), int_diff(denominator)])
  print(diff_list)

  # return higher value - difference between higher and lower
  return diff_list[0] + abs((diff_list[0] - diff_list[1]))
  '''

  # iterate through numerator and denominator values individually
  distance_counter = 0
  for point in range(len(numerator)-1):
    '''
    print("x = {}\ny = {}\n".format(numerator[point], denominator[point]))
    '''
    num_diff = abs(numerator[point] - numerator[point+1])
    den_diff = abs(denominator[point] - denominator[point+1])
    if den_diff > num_diff: 
      num_diff += den_diff - num_diff
    distance_counter += num_diff
    diff_str = "x[n]: {} => x[n+1]: {} => {}\n".format(numerator[point], numerator[point+1], num_diff)
    diff_str += "y[n]: {} => y[n+1]: {}\n".format(denominator[point], denominator[point+1])
    print(diff_str)
    
  print("[Total]: {}".format(distance_counter))



if __name__=="__main__":
  print(minTimePoints(sys.argv[1]))
