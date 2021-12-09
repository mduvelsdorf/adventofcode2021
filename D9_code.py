import os
import numpy as np

cwd = os.getcwd()
file = open(cwd+"\D9_data")
floor = []
for line in file:
    floor.append([int(x) for x in line.replace("\n","")])
floor = np.array(floor)

#Recursive function - looks for values greater than but not equal to 9 based on the starting point
#Continues checking all nearby points until out of the array or equals 9
#Adds coordinates to a list
def checkBasin(arr,x,y,item):
    height, length = np.shape(arr)
    if x < height and y < length and not (item == 9):
        size = [(x, y)]
        # Check left.
        if y > 0:
            if (arr[x, y - 1] > item):
                size += checkBasin(arr, x, y - 1, arr[x, y - 1])

        # Check right.
        if y < (length - 1):
            if (arr[x, y + 1] > item):
                size += checkBasin(arr, x, y + 1, arr[x, y + 1])

        # Check bottom.
        if x < (height - 1):
            if (arr[x + 1, y] > item):
                size += checkBasin(arr, x + 1, y, arr[x + 1, y])

        # Check top.
        if x > 0:
            if (arr[x - 1, y] > item):
                size += checkBasin(arr, x - 1, y, arr[x - 1, y])
    else:
        size = ()

    return size

#Check array for the lowest point to find surrounding basin values
#All surrounding vertical/horizontal points must be greater than value
#Triggers the check basin function when a low point is found
def checkLowPoints(arr):
    height, length = np.shape(arr)
    lowPoints = []
    basin = []
    for (x, y), item in np.ndenumerate(arr):
        lowest = []
        if not item == 9:
            # Check left.
            if y > 0:
                if arr[x, y-1] > item:
                    lowest.append(True)
                else:
                    lowest.append(False)

            # Check right.
            if y < (length - 1):
                if arr[x, y+1] > item:
                    lowest.append(True)
                else:
                    lowest.append(False)

            # Check bottom.
            if x < (height - 1):
                if arr[x+1, y] > item:
                    lowest.append(True)
                else:
                    lowest.append(False)

            # Check top.
            if x > 0:
                if arr[x-1, y] > item:
                    lowest.append(True)
                else:
                    lowest.append(False)

            if all(lowest):
                lowPoints.append(item)
                basin.append(checkBasin(arr,x,y,item))

    #Use set to remove duplicate coordinates for each basin
    basin = [set(x) for x in basin]
    #Returns sum of low points plus 1 for each point (part 1)
    #Returns the size of each basin
    return np.sum(lowPoints) + len(lowPoints),[len(x) for x in basin]

lowPoints,basins = checkLowPoints(floor)

basins = sorted(basins,reverse = True)
print(lowPoints)
print(np.prod(basins[:3]))