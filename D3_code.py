import os
import numpy as np

def getNumbers():
    cwd = os.getcwd()
    file = open(cwd+"\D3_data")
    numbers = []
    for line in file:
        numbers.append(list(line.replace("\n","")))
    return numbers

numbers = np.array(getNumbers(),int)
transpose = numbers.transpose()

def part1():
    gamma = []
    epsilon = []
    for row in transpose:
        if sum(row) > (np.size(row) / 2):
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
    gamma = int("".join([str(int) for int in gamma]),2)
    epsilon = int("".join([str(int) for int in epsilon]),2)
    return gamma * epsilon

def oxygen(transpose):
    oxyTranspose = transpose.copy()
    for i in range(0,np.shape(oxyTranspose)[0]):
        if np.shape(oxyTranspose)[1] == 1:
            return oxyTranspose.transpose()
        vals,counts = np.unique(oxyTranspose[i],return_counts=True)
        if counts[0] == counts[1]:
            mode = 1
        else:
            mode = vals[np.argmax(counts)]
        oxyTranspose = np.delete(oxyTranspose,(np.where(oxyTranspose[i] != mode)[0]),axis=1)
    return int("".join([str(int) for int in oxyTranspose.flatten()]),2)

def co2(transpose):
    co2Transpose = transpose.copy()
    for i in range(0, np.shape(co2Transpose)[0]):
        if np.shape(co2Transpose)[1] == 1:
            return int("".join([str(int) for int in co2Transpose.flatten()]), 2)
        vals, counts = np.unique(co2Transpose[i], return_counts=True)
        if counts[0] == counts[1]:
            mode = 0
        else:
            mode = vals[np.argmin(counts)]
        co2Transpose = np.delete(co2Transpose, (np.where(co2Transpose[i] != mode)[0]), axis=1)
    print(co2Transpose)
    return int("".join([str(int) for int in co2Transpose.flatten()]), 2)

print(oxygen(transpose) * co2(transpose))