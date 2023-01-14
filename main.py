import matplotlib.pyplot as plt
import numpy as np
import random

def rand_pts(n):
    points = []
    for i in range(n):
        x = random.uniform(0, 10)
        y = random.uniform(0, 10)
        points.append([x, y])
    return points

def leftOf(a, b, c):
    signedArea = (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
    return (signedArea > 0)

def find_lowest(pts):
  lowest = pts[0]
  for i in pts:
    if i[1] < lowest[1]:
      lowest = i
  return lowest

def sortByAngle(pts, anchor):
  slopes = {}
  for aPoint in pts:
    if aPoint[0] == anchor[0]:
      continue
    slope = (aPoint[1] - anchor[1])/(aPoint[0] - anchor[0])
    slopes[str(aPoint)] = slope
  slopes_positive = {k: v for k, v in slopes.items() if v > 0}
  slopes_negative = {k: v for k, v in slopes.items() if v < 0}
  slopes_positive = dict(sorted(slopes_positive.items(), key=lambda x: x[1]))
  slopes_negative = dict(sorted(slopes_negative.items(), key=lambda x: x[1]))
  newPts = list(slopes_positive.keys())+ list(slopes_negative.keys())
  newPts = [[float(x) for x in item.strip('[]').split(',')] for item in newPts]
  return newPts

def conv_hull(pts):
    anchor = find_lowest(pts)
    pts = sortByAngle(pts, anchor)
    pts.insert(0, anchor)
    end = pts[-1]
    start = pts[0]
    hull = []
    i = 0
    while i < len(pts):
        prev= pts[i-1]
        curr = pts[i]
        if i == len(pts)-1:
            next = pts[0]
        else:
            next = pts[i+1]
        if leftOf(prev,curr,next) == True:
            hull.append(curr)
            i += 1
        else:
            pts.pop(i)
            i -= 1

    print(hull)
    return hull,anchor

pts = rand_pts(10)

hull,anchor = conv_hull(pts)

x1, y1 = np.array(pts).T
x2, y2 = np.array(hull).T

plt.figure(figsize=(8, 8))
plt.axis('equal')
plt.scatter(x1,y1, linewidth=3)
plt.scatter(anchor[0],anchor[1],edgecolor='red', linewidth=3)
plt.fill(x2,y2, facecolor='none', edgecolor='purple', linewidth=3)
plt.show()
