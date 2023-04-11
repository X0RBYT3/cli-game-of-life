import os
import sys
import time
import argparse
from random import randint

# Function to parse command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument('-r', '--rows', type=int, default=20, help='Number of rows in the grid')
    parser.add_argument('-c', '--columns', type=int, default=50, help='Number of columns in the grid')
    parser.add_argument('-s', '--speed', type=float, default=0.1, help='Update speed in seconds')
    parser.add_argument('-i', '--iterations', type=int, default=None, help='Number of iterations to run')
    return parser.parse_args()

# Function to clear the terminal screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to create a random grid of specified size
def create_grid(rows, columns):
    return [[randint(0, 1) for _ in range(columns)] for _ in range(rows)]

# Function to print the grid on the terminal screen
def print_grid(grid):
    for row in grid:
        print(''.join(['#' if cell else ' ' for cell in row]))

# Function to count the number of live neighbors for a given cell
def count_neighbors(grid, row, col):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if (r != row or c != col) and (0 <= r < rows) and (0 <= c < cols):
                count += grid[r][c]
    return count

# Function to update the grid based on the rules of the Game of Life
def update_grid(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            neighbors = count_neighbors(grid, r, c)
            if grid[r][c] and neighbors in (2, 3):
                new_grid[r][c] = 1
            elif not grid[r][c] and neighbors == 3:
                new_grid[r][c] = 1

    return new_grid

# Main function to run the Game of Life
def main():
    args = parse_arguments()
    grid = create_grid(args.rows, args.columns)
    iteration = 0

    while args.iterations is None or iteration < args.iterations:
        clear_screen()
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(args.speed)
        iteration += 1

# Entry point of the script
if __name__ == '__main__':
    main()
