import os
import numpy as np

cwd = os.getcwd()
file = open(cwd+"\D7_data")
crabs = np.array(file.readline().split(","),int)

def part1():
    fuel = 0
    for i in range(np.amax(crabs)):
        newFuel = np.sum(abs(crabs - i))
        if i == 0 or newFuel < fuel:
            fuel = newFuel
    return fuel

print(part1())

def part2():
    fuel = 0
    for i in range(np.amax(crabs)):
        n = abs(crabs - i)
        newFuel = np.sum((n**2+n)/2)
        if i == 0 or newFuel < fuel:
            fuel = newFuel
    return int(fuel)

print(part2())