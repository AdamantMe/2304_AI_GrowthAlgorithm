from GrowthRules.BaseGrowthRule import BaseGrowthRule
import time
import os
import random

class ProbabilisticGrowthRule(BaseGrowthRule):
    def __init__(self):
        self.changes = True 
        self.min_iterations = 5  #Minimum number of iterations before stopping

    def apply(self, grid):
        self.start_timer()  #Initialize the start time for benchmarking
        growth_step = 1
        self.changes = True

        #Set the initial state in the center of the grid
        grid.update_cell(grid.size // 2, grid.size // 2, growth_step)

        iterations = 0  #Track the number of iterations
        total_sleep_time = 0 #Track the total sleep time

        while self.changes or iterations < self.min_iterations:
            self.changes = False  #Reset changes at the beginning of each iteration
            new_growth = []
            iterations += 1

            #Iterate over all cells in the grid
            for i in range(grid.size):
                for j in range(grid.size):
                    if grid.get_cell(i, j) == growth_step:
                        grown_neighbors = self.count_grown_neighbors(grid, i, j)

                        #Check the four neighboring cells for potential growth
                        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            ni, nj = i + di, j + dj
                            if grid.is_valid_cell(ni, nj) and grid.get_cell(ni, nj) == 0:
                                growth_chance = 0.15 + 0.25 * grown_neighbors
                                if random.random() < growth_chance:
                                    new_growth.append((ni, nj))
                                    self.changes = True  #Set to True if there were changes to the grid

            #Update the grid with new growth
            for i, j in new_growth:
                grid.update_cell(i, j, growth_step + 1)

            #Clear the screen and print information
            self.clear_screen()
            print(f"Probabilistic Growth Algorithm - Iteration: {growth_step}")
            print("Each number represents the growth step at which the cell was added.")
            print("0: Empty cell, 1+: Growth steps\n")

            grid.print_grid()

            sleep_start_time = time.time()
            time.sleep(1)  #Pause for a second each iteration so user can see the changes
            sleep_end_time = time.time()
            total_sleep_time += sleep_end_time - sleep_start_time

            growth_step += 1

        #Benchmark calculation, subtracting the total sleep time
        elapsed_time = time.time() - self.start_time - total_sleep_time
        print(f"Probabilistic Growth Algorithm completed in {elapsed_time:.2f} seconds without counting sleep time.")

    def clear_screen(self):
        """Clears the terminal screen. This method is platform-dependent."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def count_grown_neighbors(self, grid, x, y):
        """Counts the number of grown neighbor cells around the cell at (x, y)."""
        count = 0
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = x + di, y + dj
            if grid.is_valid_cell(ni, nj) and grid.get_cell(ni, nj) > 0:
                count += 1
        return count

    def start_timer(self):
        """Starts a timer for the benchmark."""
        self.start_time = time.time()
