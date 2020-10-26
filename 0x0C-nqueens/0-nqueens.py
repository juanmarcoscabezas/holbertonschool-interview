#!/usr/bin/python3

"""
N queens problem
"""

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        n_q = int(sys.argv[1])
    except BaseException:
        print('N must be a number')
        sys.exit(1)

    if n_q < 4:
        print('N must be at least 4')
        sys.exit(1)

    board = [[0 for col in range(n_q)] for row in range(n_q)]

    def is_attack(i, j):
        for k in range(n_q):
            if board[i][k] == 1 or board[k][j] == 1:
                return True
        for k in range(n_q):
            for l in range(n_q):
                if ((k + l) == (i + j)) or ((k - l) == (i - j)):
                    if board[k][l] == 1:
                        return True
        return False

    def n_queen(n):
        if n == 0:
            return True
        for i in range(n_q):
            for j in range(n_q):
                if (not(is_attack(i, j))) and (board[i][j] != 1):
                    board[i][j] = 1
                    if n_queen(n - 1):
                        return True
                    board[i][j] = 0
        return False

    n_queen(n_q)
    print(board)
