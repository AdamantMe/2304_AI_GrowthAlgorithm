import os
import random
import time

from GrowthRules.BaseGrowthRule import BaseGrowthRule

class DiffusionGrowthRule(BaseGrowthRule):
    def __init__(self):
        self.changes = True

    def apply(self, grid):
        self.start_timer()
        growth_step = 1
        self.changes = True
        max_distance = grid.size // 2  #Maximum diffusion distance

        #Set the initial state in the center of the grid
        initial_x, initial_y = grid.size // 2, grid.size // 2
        grid.update_cell(initial_x, initial_y, growth_step)

        total_sleep_time = 0
        while self.changes:
            self.changes = False
            new_growth = []

            #Iterate over all cells in the grid for the current growth step
            for i in range(grid.size):
                for j in range(grid.size):
                    if grid.get_cell(i, j) == growth_step:
                        #Check neighboring cells for potential growth
                        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            ni, nj = i + di, j + dj
                            if grid.is_valid_cell(ni, nj) and grid.get_cell(ni, nj) == 0:
                                distance = abs(ni - initial_x) + abs(nj - initial_y)
                                growth_chance = 1 - (distance / (max_distance * 2))
                                if random.random() < growth_chance:
                                    new_growth.append((ni, nj))
                                    self.changes = True

            #Update the grid with new growth for the next step
            for i, j in new_growth:
                grid.update_cell(i, j, growth_step + 1)

            self.clear_screen()
            print(f"Diffusion Growth Algorithm - Iteration: {growth_step}")
            print("Each number represents the growth step at which the cell was added.")
            print("0: Empty cell, 1+: Growth steps\n")

            grid.print_grid()

            sleep_start_time = time.time()
            time.sleep(1) 
            sleep_end_time = time.time()
            total_sleep_time += sleep_end_time - sleep_start_time

            if self.changes:
                growth_step += 1

            if growth_step > max_distance:  #Limit the growth to the maximum distance
                break

        elapsed_time = time.time() - self.start_time - total_sleep_time
        print(f"Diffusion Growth Algorithm completed in {elapsed_time:.2f} seconds without counting sleep time.")

    def start_timer(self):
        self.start_time = time.time()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
