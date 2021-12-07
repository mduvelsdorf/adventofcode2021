import os
import numpy as np

def getNumbers():
    cwd = os.getcwd()
    file = open(cwd+"\D4_data")
    numbers = file.readline().split(",")
    numbers = [int(num) for num in numbers]
    cards = []
    for line in file:
        cards.append(line.replace("\n","").split())
    return numbers, cards

numbers, cards = getNumbers()

def bingoWin(numbers, cards):
    score = 0
    win = len(numbers)
    for i in range(0,len(cards),6):
        card = np.array((cards[i+1],cards[i+2],cards[i+3],cards[i+4],cards[i+5]),int).flatten().reshape(5,5)
        def game(card):
            for j in range(len(numbers)):
                card = np.where(card == numbers[j],-1,card)
                for k in range(5):
                    row = np.prod(card[k,:])
                    column = np.prod(card[:,k])
                    if row == -1 or column == -1:
                        card = np.where(card == -1,0,card)
                        newScore = np.sum(card)
                        newWin = j
                        return newScore, newWin
        newScore, newWin = game(card)
        if newWin < win:
            score = newScore
            win = newWin
    return score, win, numbers[win], score * numbers[win]

print(bingoWin(numbers, cards))

def bingoLose(numbers, cards):
    score = 0
    win = 0
    for i in range(0,len(cards),6):
        card = np.array((cards[i+1],cards[i+2],cards[i+3],cards[i+4],cards[i+5]),int).flatten().reshape(5,5)
        def game(card):
            for j in range(len(numbers)):
                card = np.where(card == numbers[j],-1,card)
                for k in range(5):
                    row = np.prod(card[k,:])
                    column = np.prod(card[:,k])
                    if row == -1 or column == -1:
                        card = np.where(card == -1,0,card)
                        newScore = np.sum(card)
                        newWin = j
                        return newScore, newWin
        newScore, newWin = game(card)
        if newWin > win:
            score = newScore
            win = newWin
    return score, win, numbers[win], score * numbers[win]

print(bingoLose(numbers, cards))