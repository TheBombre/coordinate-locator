from random import randint
from sys import argv


def create_grid(col_num, row_num):
    if len(argv) >= 3:
        col_num = int(argv[1])
        row_num = int(argv[2])

    grid = []
    for i in range(row_num):
        temp_row = []
        for i in range(col_num):
            temp_row.append('O')
        grid.append(temp_row)
    return grid


default_grid = create_grid(10, 10)

row_num = len(default_grid)
col_num = len(default_grid[0])

guesses = int((len(default_grid)*len(default_grid[0]))/2)

computer_position_row = randint(1, row_num)
computer_position_col = randint(1, col_num)


def x_marker():
    default_grid[computer_position_row - 1][computer_position_col - 1] = 'X'


def show_grid():
    for i in range(len(default_grid)):
        print(' '.join(default_grid[i]))
    print('row: ', computer_position_row)
    print('col: ', computer_position_col)


x_marker()

while guesses > 0:
    print('Games left: ', guesses)

    row = int(input('Guess the row from 1 to ' + str(row_num) + ':'))
    col = int(input('Guess the col from 1 to ' + str(col_num) + ':'))

    if (row > row_num or col > col_num):
        guesses -= 1
        print('Those coordinates are not on the grid')
        print('\n')
        continue

    elif (row == computer_position_row) and (col == computer_position_col):
        show_grid()
        print('You Won!!')
        break

    else:
        guesses -= 1
        print('Sorry you didn\'t find the ship. Try Again')
        print('\n')
        continue

else:
    print('Game Over')
    show_grid()
