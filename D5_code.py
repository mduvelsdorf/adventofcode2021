import os
import numpy as np

def getCoords():
    cwd = os.getcwd()
    file = open(cwd+"\D5_data")
    coordinates = []
    for line in file:
        coordinate = line.replace(" -> ",",").split(",")
        coordinates.append(coordinate)
    return np.array(coordinates,int)

coordinates = getCoords()

shape = np.amax(coordinates)+1

field = np.zeros((shape,shape))

for coord in coordinates:
    if coord[0] == coord[2]:
        minimum = min(coord[1], coord[3])
        maximum = max(coord[1], coord[3])
        field[minimum:maximum+1,coord[0]] += 1
    elif coord[1] == coord[3]:
        minimum = min(coord[0],coord[2])
        maximum = max(coord[0],coord[2])
        field[coord[1],minimum:maximum+1] += 1
    else:
        xMin = min(coord[0], coord[2])
        yMin = min(coord[1], coord[3])
        xMax = max(coord[0], coord[2])
        yMax = max(coord[1], coord[3])
        for i in range(xMax-xMin+1):
            if coord[1] == yMin and coord[0] == xMin:
                field[coord[1]+i,coord[0]+i] += 1
            elif coord[1] == yMin and coord[0] == xMax:
                field[coord[1]+i,coord[0]-i] += 1
            elif coord[1] == yMax and coord[0] == xMin:
                field[coord[1]-i, coord[0]+i] += 1
            else:
                field[coord[1]-i, coord[0]-i] += 1

print(field)
print((field > 1).sum())

