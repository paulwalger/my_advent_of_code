class Octopus:
    def __init__(self, x, y, energy_level) -> None:
        self.x = x
        self.y = y
        self.energy_level = energy_level
        self.has_flashed = False

    def __str__(self) -> str:
        return f"({self.x}, {self.y}) {self.energy_level}"

    def get_adjacents_octopus(self, grid):
        vectors = {(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, 1), (1, -1)}
        width = len(grid[0])
        height = len(grid)
        adjacents = []
        for x_off, y_off in vectors:
            if self.x + x_off >= 0 and self.x + x_off < width and self.y + y_off >= 0 and self.y + y_off < height:
                adjacents.append(grid[self.x + x_off][self.y + y_off])
        return adjacents

    def flash_and_propagate(self, grid):
        if self.energy_level > 9 and not self.has_flashed:
            self.has_flashed = True
            for octopus in self.get_adjacents_octopus(grid):
                octopus.energy_level += 1
                octopus.flash_and_propagate(grid)

    def reset(self):
        if self.has_flashed:
            self.has_flashed = False
            self.energy_level = 0


def get_octopus_grid(file_name):
    with open(file_name, "r") as input_file:
        grid = []
        for x, line in enumerate(input_file):
            grid.append(list([Octopus(x, y, energy_level) for y, energy_level in enumerate(map(int, line.strip()))]))
    return grid


def count_flash_next_step(grid):
    count = 0

    # increase energy level by 1
    for line in grid:
        for octopus in line:
            octopus.energy_level += 1

    # propagate flashes
    for line in grid:
        for octopus in line:
            octopus.flash_and_propagate(grid)

    # count step flashes and reset
    for line in grid:
        for octopus in line:
            if octopus.has_flashed:
                count += 1
                octopus.reset()

    return count


def count_flashes_for_nb_steps(grid, nb_step):
    return sum(count_flash_next_step(grid) for _ in range(nb_step))


def first_step_all_flashes(grid):
    size_grid = len(grid) * len(grid[0])
    nb_flash_step = 0
    nb_step = 0
    while size_grid != nb_flash_step:
        nb_step += 1
        nb_flash_step = count_flash_next_step(grid)
    return nb_step


grid = get_octopus_grid("input.txt")
print(f"Number of flash after 100 steps: {count_flashes_for_nb_steps(grid, 100)}")
grid = get_octopus_grid("input.txt")
print(f"First step where all octopus flashes: {first_step_all_flashes(grid)}")
