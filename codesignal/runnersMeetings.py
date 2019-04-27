import numpy as np
import scipy.linalg as la
import math
def runnersMeetings(startPosition, speed):
  speedCount = 0

  for i in range(len(speed)-1):
    if speed[i] == speed[i+1]:
      speedCount += 1
  if speedCount == len(speed) -1:
    return -1

  A = np.array([[speed[0],-1],[speed[1],-1]])
  B = np.array([-1*startPosition[0],-1*startPosition[1]])
  ans = la.solve(A, B)
  print(round(ans[0],50))
  frac,num = math.modf(ans[0])
  fracStr = str(frac)
  idx = fracStr.find(".")
  print(fracStr[idx+1:])
  length = len(fracStr[idx+1:])
  arr = []
  finAns = {}


  for i in range(len(speed)):
    temp = speed[i] * round(ans[0],length) + startPosition[i]
    #print(temp)
    arr.append(temp)

  for x in arr:
    if x not in finAns:
      finAns[x] = 1
    else:
      finAns[x] += 1
  
  largest = 0

  for x in finAns.values():
    if x > largest:
      largest = x
  
  #print(largest)
  if largest >= 2:
    return largest
  else:
    return -1




print(runnersMeetings([1, 4, 2], [5, 6, 2]))