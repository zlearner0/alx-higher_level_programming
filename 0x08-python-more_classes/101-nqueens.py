#!/usr/bin/python3
'''this is documentation for the created module
'''

import sys


def solve_n_queens(n):
    '''function to solve N queen puzzle'''
    solutions = []
    positions = [-1] * n
    solve_n_queens_helper(n, 0, positions, solutions)
    return solutions


def solve_n_queens_helper(n, row, positions, solutions):
    '''helper mothed for solving queens pusszle'''
    if row == n:
        solutions.append([(i, positions[i]) for i in range(n)])
    else:
        for col in range(n):
            if is_valid(row, col, positions):
                positions[row] = col
                solve_n_queens_helper(n, row + 1, positions, solutions)


def is_valid(row, col, positions):
    '''method that check the validity for the gird'''
    for r, c in enumerate(positions):
        if c == col or r + c == row + col or r - c == row - col:
            return False
    return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_n_queens(n)

    for sol in solutions:
        print(sol)
