# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 15:21:51 2023

@author: 33670
"""

'''
Upgrades : 
    Error go back
'''

# imports


# functions




import time
import random
import keyboard
import os
import numpy as np
from operator import itemgetter
def getData(filename, data):
    with open(filename, 'r') as myData:
        for line in myData:
            data.append(line)


def writeData(filename, data):
    with open(filename, 'a') as myData:
        for (nickname, score) in data:
            myData.write(f'{nickname} {score}\n')


def showHighScores(nickname=None, bad=False):
    tempVariable = []
    getData('HIGH_SCORES_TABLE.txt', tempVariable)
    tempVariable = cleanHighScores(tempVariable)
    tempVariable = sorted(tempVariable, key=itemgetter(1), reverse=bad)
    if not bad:
        if nickname != None:
            tempVariable = elementsIn(
                tempVariable, condition=lambda element: element[0] == nickname)
            print("Your high scores : \n")
            displayHighScores(tempVariable)
        else:
            print("The best-of all :\n")
            displayHighScores(tempVariable)
    else:
        if nickname != None:
            tempVariable = elementsIn(
                tempVariable, condition=lambda element: element[0] == nickname)
            print("Your worst scores : \n")
            displayHighScores(tempVariable)
        else:
            print("The worst-of all :\n")
            displayHighScores(tempVariable)


def cleanHighScores(array):
    tempArray = []
    for line in array:
        tempArray.append(line.strip().split(' '))

        # set as float for the sorted later
        tempArray[-1][-1] = float(tempArray[-1][-1])
    return tempArray


def elementsIn(elements, condition=lambda x: True):
    returnList = []
    for element in elements:
        if condition(element):
            returnList.append(element)
    return returnList


def displayHighScores(scores):
    if len(scores) <= 5:
        for (index, (nickname, score)) in enumerate(scores):
            print(f'\t{index+1} - {nickname} : {score} s')
    else:
        for (index, (nickname, score)) in enumerate(scores[:5]):
            print(f'\t{index+1} - {nickname} : {score} s')
    print('\n')


def visibility(character='\n'):
    if character != '#':
        print(character)
    else:
        print(character*65)


def clear():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')

    # For macOS and Linux
    else:
        _ = os.system('clear')


def numberCharacters(sentence):
    number = 0
    for character in sentence:
        if character in AVAILABLE_CHARACTERS or character == ' ':
            number += 1
    return number


def timePerCharacter(timer: float, numberOfCharacters: int = 1):
    try:
        return round(timer/numberOfCharacters, 2)
    except ValueError:
        print(
            f'ERROR in numberCharacters given in timePerCharacter : numberCharacters = {numberCharacters}')


def timer():
    clear()
    print("Are you ready ???!")
    time.sleep(1)

    clear()
    print("3 ...")
    time.sleep(1)

    clear()
    print("2 ..")
    time.sleep(1)

    clear()
    print("1 .")
    time.sleep(1)

    clear()


def rules():
    while True:
        try:
            print("The rules are simple :")
            print("\t- you have to rewrite the sentence")
            print("\t- punctuation marks are not asked, EXCEPT spaces")
            print("\t- majuscule and minuscule are different letters\n")

            answer = str(input("Did you get it ? (Y/N) : "))

            if answer != 'Y':
                raise ValueError
                clear()
            break

        except:
            print(
                "\n\nThen ask Raynor (aka Romain ETIENNE) or another player of this game.\n\n")
            time.sleep(2)
            clear()
    clear()


# variables
AVAILABLE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
SENTENCES_DATA = []
HIGH_SCORES_TABLE = []
NICKNAME = None

if __name__ == '__main__':

    clear()
    visibility('#')

    # taking our data from DATA.txt
    getData('DATA.txt', SENTENCES_DATA)

    # nickname ?
    while True:
        try:
            NICKNAME = str(input("\nYour nickname ? : "))
            if NICKNAME == '':
                raise ValueError
            break
        except:
            print("Not a correct nickname.")
            time.sleep(2)
            clear()

    clear()
    visibility()

    rules()

    # how many mini-game ?
    while True:
        try:
            numberOfGames = int(input("How many games ? : "))
            break
        except ValueError:
            print("Sry, I need a number.\n")
            time.sleep(2)
            clear()

    clear()
    visibility()

    for game in range(numberOfGames):
        # run the mini-game
        index = random.randint(0, len(SENTENCES_DATA)-1)
        sentence = SENTENCES_DATA[index]

        timer()

        print(sentence)
        t_start = time.time()

        for (i, letter) in enumerate(sentence):
            while keyboard.read_key() != letter:
                if letter not in AVAILABLE_CHARACTERS:
                    if letter == ' ':
                        while keyboard.read_key() != 'space':
                            print('_'*i + sentence[i:])
                        break
                    break
                print('_'*i + sentence[i:])

        t_end = time.time()
        t_total = t_end - t_start

        timeHighScores = timePerCharacter(t_total, numberCharacters(sentence))

        clear()
        visibility()

        HIGH_SCORES_TABLE.append([NICKNAME, timeHighScores])
        print(f'Done in : {timeHighScores}s')

    if HIGH_SCORES_TABLE != []:
        print('\n\nFinal scores :\n')
        displayHighScores(HIGH_SCORES_TABLE)
        writeData('HIGH_SCORES_TABLE.txt', HIGH_SCORES_TABLE)

    showHighScores(nickname=NICKNAME)

    if NICKNAME != None:
        showHighScores()
        showHighScores(bad=True)

    visibility('#')
