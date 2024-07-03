#!/usr/bin/python3
""" N queens problem """
import sys


def print_board(board):
    """ Print the board """
    matrix = []
    for i, row in enumerate(board):
        row_list = []
        for j, col in enumerate(row):
            if col == 1:
                row_list.append(i)
                row_list.append(j)
        matrix.append(row_list)
    print(matrix)

def is_safe(board, row, col):
    """ Check if a queen can be placed on board[row][col] """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_n_queens_poss(board, col, size):
    """ Possibilities to solve the N queens problems
    args:
    size: length of the board
    """
    if col == len(board):
        print_board(board)
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_n_queens_poss(board, col + 1, size) or res
            board[i][col] = 0
    return res

def solve_n_queens(size):
    """ Solve the N queens problems
    args:
    size: length of the board
    """
    board = [[0 for i in range(size)] for j in range(size)]
    if not solve_n_queens_poss(board, 0, size):
        print("Solution does not exist")
        return False
    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    size = int(sys.argv[1])
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve_n_queens(size)
