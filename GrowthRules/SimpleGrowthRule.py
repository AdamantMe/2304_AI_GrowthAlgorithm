from GrowthRules.BaseGrowthRule import BaseGrowthRule
import time
import os

class SimpleGrowthRule(BaseGrowthRule):
    def __init__(self):
        self.changes = True  #Initialize changes to True
        self.start_time = None  #Variable to store the start time

    def apply(self, grid):
        growth_step = 1
        self.changes = True  #Reset changes at the beginning of each iteration
        self.start_time = time.time()  #Record the start time
        total_sleep_time = 0  #Variable to store the total sleep time

        while self.changes:
            self.changes = False
            new_growth = []

            for i in range(grid.size):
                for j in range(grid.size):
                    if grid.get_cell(i, j) == growth_step:
                        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            if grid.is_valid_cell(i + di, j + dj) and grid.get_cell(i + di, j + dj) == 0:
                                new_growth.append((i + di, j + dj))
                                self.changes = True

            for i, j in new_growth:
                grid.update_cell(i, j, growth_step + 1)

            #Clear the screen and print information
            self.clear_screen()
            print(f"Simple Growth Algorithm - Iteration: {growth_step}")
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
        print(f"Simple Growth Algorithm completed in {elapsed_time:.2f} seconds. Note: Each iteration sleeps for 1 second for visualization.")

    def clear_screen(self):
        """Clears the terminal screen. This method is platform-dependent."""
        os.system('cls' if os.name == 'nt' else 'clear')