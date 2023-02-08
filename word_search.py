import random
import string
from random import choice

RIGHT = (1,0)
DOWN = (0,1)
RIGHT_DOWN = (1,1)
RIGHT_UP = (1, -1)
DIRECTIONS = (RIGHT, DOWN, RIGHT_DOWN, RIGHT_UP)

def get_size(grid):
    """ This function is for calculating the width and height of the grid.
        The width means number of letters in a list, and the height means number of lists.
        Input: a letter grid in the list-of-lists-of-letters format
        Return: a tuple (width, height) """

    W = len(grid[0])
    H = len(grid)
    return (W, H)


def print_word_grid(grid):
    """ This function is for printing the input grid in a dense format.
        Input: a letter gird
        Return: no return value, print dense grid """

    width_height = get_size(grid)
    dense = ""
    for i in range(0, width_height[1]):
        subgrid = grid[i]
        for j in range(0, width_height[0]):
            dense += subgrid[j]
        if i < (width_height[1] - 1):
            dense += "\n"
    print(dense)

def copy_word_grid(grid):
    """ This function is for copy the input grid.
        Input: a letter grid
        Return: a copy of an input grid """

    width_height = get_size(grid)
    width = width_height[0]
    height = width_height[1]
    copygrid = grid.copy()
    for i in range(0, height):
        for j in range(0, width):
            copygrid[i] = grid[i].copy()
    return copygrid

def extract(grid, position, direction, max_len):
    """ This function is for extracting a word from an input grid according to given directions.
        Input:
            grid = a letter grid
            position = a tuple [row, column] indicating starting position
            direction = a variable name calling saved tuple, indicating moving direction
            max_len = an integer indicating number of extract word
        Return: a string """

    column_count = position[0]
    row_count = position[1]
    width_height = get_size(grid)
    counter = 0
    answer = ""
    while (0 <= row_count < width_height[1]) and (0 <= column_count < width_height[0]) and (counter < max_len):
        answer += grid[row_count][column_count]
        row_count = row_count + direction[1]
        column_count = column_count + direction[0]
        counter += 1
    return answer

def show_solution(grid, word, solution):
    """ This function finds the word in grid according to the suggested solution.
        If the word is found, the function shows a sentence that the word is found and shows grid with a capitalized word.
        If the function fails to find the word, it shows a sentence that the word is not found. """

    if bool(solution) == False:
        return print(word, "is not found in this word search")

    copygrid = copy_word_grid(grid)
    position = solution[0]
    direction = solution[1]
    column_count = position[0]
    row_count = position[1]
    direction_col = direction[0]
    direction_row = direction[1]
    counter = 0
    grid_size = get_size(copygrid)

    user_solution = extract(grid, position, direction, len(word))

    if word != user_solution:
        print(word, "is not found in this word search")
    else:
        word = word.upper()
        print(word, "can be found as below")
        while (0 <= row_count < grid_size[1]) and (0 <= column_count < grid_size[0]) and (counter <= (len(word) - 1)):
            copygrid[row_count][column_count] = grid[row_count][column_count].upper()
            column_count = column_count + direction_col
            row_count = row_count + direction_row
            counter += 1
        print_word_grid(copygrid)


def find(grid, word):
    """ This function finds word in grid.
        If the word is found, the function returns solution of the word, which includes location and direction of the word.
        If the word is not found, the function returns False. """

    word_length = len(word)
    first_letter = word[0]
    possible_startpoint = []
    width_height = get_size(grid)

    for i in range(0, width_height[1]):
        for j in range(0, width_height[0]):
            if grid[i][j] == first_letter:
                possible_startpoint.append((j, i))

    position_direction = []
    for k in range(0, len(possible_startpoint)):
        column_count = possible_startpoint[k][0]
        row_count = possible_startpoint[k][1]
        for l in DIRECTIONS:
            letter_end_c = column_count + (l[0] * (word_length - 1))
            letter_end_r = row_count + (l[1] * (word_length - 1))
            if (-1 < letter_end_c < width_height[0]) and (-1 < letter_end_r < width_height[1]):
                position_direction.append((possible_startpoint[k], l))

    answer =""
    for m in range(0, len(position_direction)):
        direction = position_direction[m][1]
        column_count = position_direction[m][0][0]
        row_count = position_direction[m][0][1]
        for o in range(0, word_length):
            answer += grid[row_count][column_count]
            column_count += direction[0]
            row_count += direction[1]
        if answer == word:
            return position_direction[m]
        else:
            answer = ""
    return bool()

def find_all(grid,words):
    """ This function is basically same with the function find.
        But, it treats a list of words and returns words found in gird and their locations and directions as a dictionary format. """

    solution_dict = {}

    for i in range(0, len(words)):
        x = find(grid, words[i])
        solution_dict[words[i]] = x
    if solution_dict == {}:
        return bool()
    else:
        return solution_dict

def find_random(width, height, target_word):
    """ This function helps the function generate.
        It finds random location and random position for a target word.
        If random function fails to find find proper location and position more than 100, it gives up to find and return False."""

    random_col = random.randint(0, width)
    random_row = random.randint(0, height)
    direction = random.choice(DIRECTIONS)
    end_col = random_col + (direction[0] * len(target_word)-1)
    end_row = random_row + (direction[1] * len(target_word)-1)

    counter = 0
    while (-1 >= end_col) or (end_col >= width) or (-1 >= end_row) or (end_row >= height):
        counter += 1
        if counter < 100:
            random_col = random.randint(0, width)
            random_row = random.randint(0, height)
            direction = random.choice(DIRECTIONS)
            end_col = random_col + (direction[0] * len(target_word) - 1)
            end_row = random_row + (direction[1] * len(target_word) - 1)
        else:
            return bool()
    return (random_col, random_row, direction)

def generate(width, height, words):
    """ This function generates a grid by suggested width and height and fills the suggested words in grid.
        Only words which have proper location and direction can be located in the grid.
        If the function fails to find proper location or direction for a word more than 100 times, it gives up to finding.
        Words can be overlapped, if the letter is same.
        After putting words in the grid, blank space of the grid is filled by random alphabet.
        The function returns a tuple with the gird and a list of words which are actually put into the grid. """

    new_grid = []
    for i in range(0, height):
        new_grid.append([])
        subgrid = new_grid[i]
        for j in range(0, width):
            subgrid.append(" ")

    words_in_grid = []
    for k in range(0, len(words)):
        target_word = words[k]
        wid = width - 1
        hei = height - 1
        x = find_random(wid, hei, target_word)
        if x != False:
            column = x[0]
            row = x[1]
            direction = x[2]
            words_in_grid.append(target_word)
            for l in range(0, len(target_word)):
                if target_word in words_in_grid:
                    if (new_grid[row][column] != " ") and (new_grid[row][column] != target_word[l]):
                        words_in_grid.remove(target_word)
                    else:
                        column += direction[0]
                        row += direction[1]

            if target_word in words_in_grid:
                column = x[0]
                row = x[1]
                for n in range(0, len(target_word)):
                    new_grid[row][column] = target_word[n]
                    column += direction[0]
                    row += direction[1]

    for p in range(0, height):
        for q in range(0, width):
            if new_grid[p][q] == " ":
                new_grid[p][q] = random.choice(string.ascii_lowercase)

    return ((new_grid, words_in_grid))
