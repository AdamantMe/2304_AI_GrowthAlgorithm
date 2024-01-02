from GrowthRules.BaseGrowthRule import BaseGrowthRule


class SimpleGrowthRule(BaseGrowthRule):
    def apply(self, grid):
        for i in range(grid.size):
            for j in range(grid.size):
                if grid.get_cell(i, j) == 1:  # If current cell is active
                    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Four cardinal directions
                        if grid.get_cell(i + di, j + dj) == 0:  # If neighboring cell is inactive
                            grid.update_cell(i + di, j + dj, 1)  # Activate the cell
                            print(f"Grew at ({i + di}, {j + dj}) from ({i}, {j})")  # Print the growth
