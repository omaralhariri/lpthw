#!/usr/bin/env python
# Running it from inside python3 in the terminal is like running it as a module
# or a class the has methods and attributes, functions,
# python3
# >>> import ex25
# OR
# python3
# >>> form ex25 import *
# from: can't read /var/mail/ex25
# Need fixation 

def breakWords(stuff):
    # Documentation comments, which are shown when asking for helo
    # python3 -> help(ex25)
    """This function will break up words for us."""
    words = stuff.split(" ")
    return words

def sortWords(words):
    """Sort the words"""
    # Sorted() does not alter original value/variable
    return sorted(words)

def printFirstWord(words):
    """Prints the first word after popping it off."""
    # Using pop() alter the original value/variable
    word = words.pop(0)
    print(word)

def printLastWord(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sortSentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = breakWords(sentence)
    return sortWords(words)

def printFirstAndLast(sentence):
    """Prints the first and last words of the sentence."""
    words = breakWords(sentence)
    printFirstWord(words)
    printLastWord(words)

def printFirstAndLastSorted(sentence):
    """Sorts the words then prints the first and last ones."""
    words = sortSentence(sentence)
    printFirstWord(words)
    printLastWord(words)
