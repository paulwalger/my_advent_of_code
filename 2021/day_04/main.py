class Grid:
    def __init__(self, grid_lines) -> None:
        self.grid = [list(map(int, line.split())) for line in grid_lines]
        self.nb_columns = len(self.grid[0])
        self.nb_rows = len(self.grid)
        self.marked_grid = [[0 for _ in range(self.nb_columns)] for _ in range(self.nb_rows)]
        self.has_already_won = False

    def __str__(self) -> str:
        return str((self.grid, self.marked_grid))

    def has_won(self) -> bool:
        # check rows
        for row in self.marked_grid:
            if all(row):
                self.has_already_won = True
                return True
        # check columns
        for col_idx in range(self.nb_columns):
            if all([row[col_idx] for row in self.marked_grid]):
                self.has_already_won = True
                return True
        return False

    def new_draw(self, number) -> None:
        for row in range(self.nb_rows):
            for col in range(self.nb_columns):
                if self.grid[row][col] == number:
                    self.marked_grid[row][col] = 1

    def sum_unmarked_numbers(self) -> int:
        sum = 0
        for row in range(self.nb_rows):
            for col in range(self.nb_columns):
                if self.marked_grid[row][col] == 0:
                    sum += self.grid[row][col]
        return sum


# generate grids
grids = []
with open("grids.txt", "r") as grids_file:
    grid_lines = []
    for line in [line.strip() for line in grids_file]:
        if line:
            grid_lines.append(line)
        else:
            grids.append(Grid(grid_lines))
            grid_lines = []

# draw numbers
with open("draws.txt", "r") as draws_file:
    draws = []
    for line in draws_file:
        draws += list(map(int, line.strip().split(",")))

    first_winner = None
    for number in draws:
        for grid in filter(lambda grid: grid.has_already_won is False, grids):
            grid.new_draw(number)
            if grid.has_won():
                if not first_winner:
                    first_winner = grid
                    print("\nFirst Winner:")
                    print(f"Grid: {grid}")
                    print(f"Last Number: {number}")
                    sum_unmarked_numbers = grid.sum_unmarked_numbers()
                    print(f"Sum Unmarked Numbers: {sum_unmarked_numbers}")
                    print(f"Result: {number * sum_unmarked_numbers}")
                if all([grid.has_already_won for grid in grids]):
                    print("\nLast Winner:")
                    print(f"Grid: {grid}")
                    print(f"Last Number: {number}")
                    sum_unmarked_numbers = grid.sum_unmarked_numbers()
                    print(f"Sum Unmarked Numbers: {sum_unmarked_numbers}")
                    print(f"Result: {number * sum_unmarked_numbers}")
