import math
import os

cwd = os.getcwd()
file = open(cwd+"\D10_data")

#Create dictionary of points for corrupt lines and dictionary of points for incomplete lines
dict = {"(":")","[":"]","{":"}","<":">"}
corruptPoints = {")":3,"]":57,"}":1197,">":25137}
corruptPointTotal = 0
incompletePoints = {")":1,"]":2,"}":3,">":4}
incompletePointTotals = []

#Iterate through each line
for line in file:
    #Keeps track of which closing character should come next
    closing = []
    #Used later to indicate if line is corrupt or incomplete
    end = False
    line = line.replace("\n","")
    #Iterate through each character
    for char in line:
        #If character is opening, append closing char to closing list
        if char in dict.keys():
            closing.append(dict[char])
        #If not, check if it's the most recent closing character, if yes, pop it out of list
        elif char == closing[-1]:
            closing.pop()
        #Indicates corrupt line, adds points to count, breaks for reading the rest of line
        elif not char == closing[-1]:
            corruptPointTotal += corruptPoints[char]
            end = True
            break
    #If True (because corrupt) move to next line, if not, line is incomplete
    if end:
        continue
    else:
        #Reverse closing (kept track by appending and popping, most recent character is last)
        incompletePoint = 0
        closing.reverse()
        #Add points based on characters, append to list of all incomplete line scores
        for char in closing:
            incompletePoint = incompletePoint * 5 + incompletePoints[char]
        incompletePointTotals.append(incompletePoint)

#Sort to find middle value
incompletePointTotals = sorted(incompletePointTotals)

print(corruptPointTotal)
#Use divide by two and floor function to find middle index
print(incompletePointTotals[math.floor(len(incompletePointTotals)/2)])