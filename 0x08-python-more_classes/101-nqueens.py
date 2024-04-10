#!/usr/bin/python3
"""10. N queens"""

import sys


def create_new_board(n):
    """Function that creates a new nxn sized chessboard with 0's."""
    board = [[' '] * n for _ in range(n)]
    return board


def copy_board(board):
    """Function that returns a deep copy of the board"""
    return [row[:] for row in board]


def find_queen_positions(board):
    """Function that finds the positions of the queens"""
    queens_positions = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == "Q":
                queens_positions.append((row, col))
    return queens_positions


def mark_invalid_moves(board, row, col):
    """Function that marks invalid moves for a queen"""
    n = len(board)
    for r in range(n):
        board[r][col] = "x"  # Marking invalid moves in the same column
        if 0 <= row + r < n:
            board[row + r][col] = "x"  # Marking invalid moves in the same row
            if 0 <= col + r < n:
                board[row + r][col + r] = "x"  # Marking invalid moves in the diagonal (down-right)
            if 0 <= col - r < n:
                board[row + r][col - r] = "x"  # Marking invalid moves in the diagonal (down-left)
        if 0 <= row - r < n:
            board[row - r][col] = "x"  # Marking invalid moves in the same row
            if 0 <= col + r < n:
                board[row - r][col + r] = "x"  # Marking invalid moves in the diagonal (up-right)
            if 0 <= col - r < n:
                board[row - r][col - r] = "x"  # Marking invalid moves in the diagonal (up-left)


def solve_queens(board, row, queens, solutions):
    """Function that solves the puzzle with backtracking"""
    if queens == len(board):
        solutions.append(find_queen_positions(board))
        return solutions

    for col in range(len(board[row])):
        if board[row][col] == " ":
            tmp_board = copy_board(board)
            tmp_board[row][col] = "Q"
            mark_invalid_moves(tmp_board, row, col)
            solutions = solve_queens(tmp_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = create_new_board(n)
    methods = solve_queens(board, 0, 0, [])
    for sol in methods:
        print(sol)
