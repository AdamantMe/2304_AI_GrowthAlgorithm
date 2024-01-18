class Grid:

    def __init__(self, size):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
    def get_cell(self, i, j):
        if 0 <= i < self.size and 0 <= j < self.size:
            return self.grid[i][j]
        return None

    def display(self):
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))

    #Check if the specified cell coordinates are within the grid bounds.
    def is_valid_cell(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size
    
    #Update the value of the specified cell if it's within bounds.
    def update_cell(self, x, y, value):
        if self.is_valid_cell(x, y):
            self.grid[x][y] = value

    #Print the grid.
    def print_grid(self):
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))
        print()

    #Returns the current state of the grid as a list of lists.
    def get_grid_state(self):
        return self.grid
    
    #Returns the highest growth step in the grid.
    def get_highest_step(self):        
        highest_step = 0
        for row in self.grid:
            for cell in row:
                if cell > highest_step:
                    highest_step = cell
        return highest_step