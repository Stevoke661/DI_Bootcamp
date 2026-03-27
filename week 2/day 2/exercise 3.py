#logic breakdown
#exs1
import os
import time
import copy

class GameOfLife:
    def __init__(self, rows, cols, initial_state=None):
        self.rows = rows
        self.cols = cols
        # Initialize grid with 0 (dead) or 1 (alive)
        if initial_state:
            self.grid = initial_state
        else:
            self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in self.grid:
            print("".join(["█" if cell else " " for cell in row]))
        print("\n")

    def count_neighbors(self, r, c):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                
                # Check boundaries for "Fixed Border" rules
                nr, nc = r + i, c + j
                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    count += self.grid[nr][nc]
        return count

    def next_generation(self):
        new_grid = copy.deepcopy(self.grid)
        
        for r in range(self.rows):
            for c in range(self.cols):
                neighbors = self.count_neighbors(r, c)
                
                if self.grid[r][c] == 1:
                    # Rule 1 & 3: Under/Overpopulation
                    if neighbors < 2 or neighbors > 3:
                        new_grid[r][c] = 0
                    # Rule 2: Lives on (no change needed)
                else:
                    # Rule 4: Reproduction
                    if neighbors == 3:
                        new_grid[r][c] = 1
                        
        self.grid = new_grid

# Example Initial State: A "Glider"
glider = [[0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0],
          [0, 1, 1, 1, 0],
          [0, 0, 0, 0, 0]]

game = GameOfLife(5, 5, glider)

# Run for 10 generations
for _ in range(10):
    game.display()
    game.next_generation()
    time.sleep(0.5)