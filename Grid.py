class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def update_cell(self, i, j, value):
        if 0 <= i < self.size and 0 <= j < self.size:
            self.grid[i][j] = value

    def get_cell(self, i, j):
        if 0 <= i < self.size and 0 <= j < self.size:
            return self.grid[i][j]
        return None

    def display(self):
        for row in self.grid:
            print(' '.join(str(cell) for cell in row))