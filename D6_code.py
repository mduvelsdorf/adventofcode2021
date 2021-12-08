import os
import numpy as np

cwd = os.getcwd()
file = open(cwd+"\D6_data")
fish = file.readline().split(",")
fish = [int(x) for x in fish]

def numpyFish(fish,rng):
    fish = np.array(fish,int)
    for i in range(rng):
        newFish = np.sum(fish == 0)
        fish = np.where(fish == 0,6,fish-1)
        fish = np.append(fish,np.full(newFish,8))
    return len(fish)

#print(numpyFish(fish,80))

def dictFish(fish,rng):

    keys = range(9)
    dict = {}
    dict = dict.fromkeys(keys)
    newFish = {}
    for i in range(9):
        dict[i] = fish.count(i)
    for i in range(rng):
        newFish[0] = dict[1]
        newFish[1] = dict[2]
        newFish[2] = dict[3]
        newFish[3] = dict[4]
        newFish[4] = dict[5]
        newFish[5] = dict[6]
        newFish[6] = dict[0] + dict[7]
        newFish[7] = dict[8]
        newFish[8] = dict[0]
        dict = newFish.copy()
    return sum(dict.values())

print(dictFish(fish,256))