from word_search import *

if __name__ == '__main__':
    print("How many rows do you want to have? Type number only.")
    height = int(input())
    print("How many columns do you want to havw? Type number only.")
    width = int(input())

    words = []
    print("What word do you want to put? Type only one word.")
    x = input()
    while x != "END":
        print("What word do you want to put? Write END if you finish.")
        words.append(x)
        x = input()

    result = generate(width, height, words)
    print_word_grid(result[0])
    print("Words", result[1], "are in your wordsearch.")
