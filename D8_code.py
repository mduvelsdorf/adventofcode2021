import os

cwd = os.getcwd()
file = open(cwd+"\D8_data")
outputValue = 0

for line in file:
    keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    dict = dict.fromkeys(keys)
    digits = line.split()[:10]
    digits = [list(x) for x in digits]
    outputs = line.split()[-4:]
    outputs = ["".join(sorted(list(x))) for x in outputs]
    counts = [len(x) for x in digits]
    dict[1] = sorted(digits[counts.index(2)])
    dict[4] = sorted(digits[counts.index(4)])
    dict[7] = sorted(digits[counts.index(3)])
    dict[8] = sorted(digits[counts.index(7)])
    for i in range(10):
        if counts[i] == 6 and all(elem in digits[i] for elem in digits[counts.index(4)]):
            dict[9] = sorted(digits[i])
        elif counts[i] == 6 and all(elem in digits[i] for elem in digits[counts.index(2)]):
            dict[0] = sorted(digits[i])
        elif counts[i] == 6:
            dict[6] = sorted(digits[i])
    for i in range(10):
        if counts[i] == 5 and all(elem in digits[i] for elem in digits[counts.index(2)]):
            dict[3] = sorted(digits[i])
        elif counts[i] == 5 and all(elem in dict[9] for elem in digits[i]):
            dict[5] = sorted(digits[i])
        elif counts[i] == 5:
            dict[2] = sorted(digits[i])
    newDict = {}
    for key,value in dict.items():
        newDict["".join(value)] = key
    newValue = []
    for output in outputs:
        newValue.append(str(newDict[output]))
    newValue = int("".join(newValue))
    outputValue += newValue

print(outputValue)

#counts = [len(x) for x in digits]
#criteria = [2,3,4,7]
#counter = len([x for x in counts if x in criteria])