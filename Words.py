import random

from Util import *






includeTwoVowels = False

excludeVeryShort = True
excludeVeryLong = True
excludeTwoVowels = False
excludeTwoConsonants = True
excludeR = True
excludeH = True
excludeC = True
excludeQ = True
excludeG = True
excludeY = False
excludeLL = False

toPascal = True







source = 'source.txt'
load = 'load.txt'

def LoadSource():
    f = open(source, "r", encoding="utf-8")
    words = [KeepAlpha(word) for word in f.readlines()]
    f.close()
    return words

def LoadDictSpa():
    f = open('dictSpa.txt', "r", encoding="utf-8")
    dictSpa = [KeepAlpha(word) for word in f.readlines()]
    f.close()
    return dictSpa


def SaveSource(words):
    f = open(source, "w", encoding="utf-8")
    for word in words:
        f.write(word + '\n')
    f.close()


def LoadInput(words, dict):
    f = open(load, "r", encoding="utf-8")
    newWords = []
    for line in f.readlines():
        lineSplit = [ToSingular(KeepAlpha(w).lower(), dict) for w in line.split(' ')]
        newWords.extend(lineSplit)
    f.close()
    count = 0
    for newWord in newWords:
        if newWord != '' and newWord in dict and newWord not in words:
            words.append(newWord)
            count += 1
    print("New words loaded: " + str(count) + ". Total words: " + str(len(words)))


def AddWords():
    LoadInput(words, dict)
    SaveSource(words)

def PassFilter(word):
    if includeTwoVowels and not HasTwoVowels(word):
        return False
    if excludeVeryShort and IsVeryShort(word):
        return False
    if excludeVeryLong and IsVeryLong(word):
        return False
    if excludeTwoVowels and HasTwoVowels(word):
        return False
    if excludeTwoConsonants and HasTwoConsonants(word):
        return False
    if excludeR and HasRInMiddle(word):
        return False
    if excludeH and HasH(word):
        return False
    if excludeC and HasC(word):
        return False
    if excludeQ and HasQ(word):
        return False
    if excludeG and HasG(word):
        return False
    if excludeY and HasY(word):
        return False
    if excludeLL and HasLL(word):
        return False
    return True

def GenerateWords(words, wordCount, columns):
    selectedWords = []
    while len(selectedWords) < wordCount:
        newWord = words[random.randrange(len(words))]
        if PassFilter(newWord) and newWord not in selectedWords:
            selectedWords.append(newWord)
    for w in selectedWords:
        if toPascal:
            w = ToPascalCase(w)
        print(w)
    random.shuffle(selectedWords)
    # print('---')
    for w in selectedWords:
        if toPascal:
            w = ToPascalCase(w)
        print(w)


words = LoadSource()
dict = LoadDictSpa()


# AddWords()
GenerateWords(words, 10, 2)