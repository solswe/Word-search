from word_search import *

if __name__ == '__main__':
    print("How many rows your wordsearch has? Type number only.")
    height = int(input())
    print("How many columns your wordsearch has? Type number only.")
    width = int(input())

    wordgrid = []
    for i in range(0, height):
        wordgrid.append([])
        subgrid = wordgrid[i]
        for j in range(0, width):
            subgrid.append("")

    print("Now Enter your wordsearch.")
    for k in range(0, height):
        for l in range(0, width):
            print("Write a letter for ", l+1, "th row and ", k+1, "th column.")
            wordgrid[k][l] += input()

    words_list = []
    print("How many words in your wordsearch?")
    num_words = int(input())
    for m in range(0, num_words):
        print("Enter words in your wordsearch.")
        words_list.append(input())

    x = find_all(wordgrid, words_list)
    words_key = list(x.keys())
    words_value = list(x.values())
    directions = {(1, 0) : "right", (0, 1) : "down", (1, 1) : "right down", (1, -1) : "right up"}
    for n in range(0, len(words_key)):
        if words_value[n] != False:
            column = words_value[n][0][0]
            row = words_value[n][0][1]
            direction = words_value[n][1]
            print(words_key[n], "is started from ", column+1, "th column and ", row+1, "th row.", end="")
            print(" Move to", directions[direction], ".")
        else:
            print(words_key[n], "is not found.")
