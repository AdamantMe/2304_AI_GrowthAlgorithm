import random

from Grid import Grid

class GrowthAlgorithm:
    def __init__(self, grid_size, growth_rule):
        self.grid = Grid(grid_size)
        self.growth_rule = growth_rule
        self.highest_step = 0  #Initialize highest_step

    def set_initial_state(self):
        middle = self.grid.size // 2
        self.grid.update_cell(middle, middle, 1)
        self.highest_step = 1  #Initially set to 1 

    def apply_growth_rules(self):
        self.growth_rule.apply(self.grid)
        highest_step_in_grid = self.grid.get_highest_step()
        if highest_step_in_grid > self.highest_step:
            self.highest_step = highest_step_in_grid

    def display_structure(self):
        self.grid.print_grid()

    def get_highest_step(self):
        return self.highest_step 