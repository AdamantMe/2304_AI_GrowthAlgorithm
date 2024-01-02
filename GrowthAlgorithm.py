import random

from Grid import Grid

class GrowthAlgorithm:
    def __init__(self, grid_size, growth_rule):
        self.grid = Grid(grid_size)
        self.growth_rule = growth_rule

    def set_initial_state(self):
        middle = self.grid.size // 2
        self.grid.update_cell(middle, middle, 1)

    def apply_growth_rules(self):
        self.growth_rule.apply(self.grid)

    def iterate_growth(self, iterations):
        for _ in range(iterations):
            self.apply_growth_rules()

    def display_structure(self):
        self.grid.display()