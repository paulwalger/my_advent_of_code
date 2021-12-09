class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class Segment:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2
        self.points = self.generate_points()

    def __str__(self) -> str:
        return f"{self.p1} -> {self.p2}"

    @property
    def is_horizontal(self):
        return self.p1.y == self.p2.y

    @property
    def is_vertical(self):
        return self.p1.x == self.p2.x

    def generate_points(self):
        s_x, s_y = 1 if self.p2.x - self.p1.x >= 0 else -1, 1 if self.p2.y - self.p1.y >= 0 else -1
        x_range = [0] * (abs(self.p2.y - self.p1.y) + 1) if self.is_vertical else range(abs(self.p2.x - self.p1.x) + 1)
        y_range = (
            [0] * (abs(self.p2.x - self.p1.x) + 1) if self.is_horizontal else range(abs(self.p2.y - self.p1.y) + 1)
        )
        return [Point(self.p1.x + s_x * x, self.p1.y + s_y * y) for x, y in zip(x_range, y_range)]


class Grid:
    def __init__(self, segments) -> None:
        self.overlaped_points = {}
        self.segments = segments

    def generate_overlaped_points(self):
        for segment in self.segments:
            for p in segment.points:
                self.overlaped_points[(p.x, p.y)] = self.overlaped_points.get((p.x, p.y), 0) + 1

    def sum_overlaped_points(self):
        sum = 0
        for nb_overlap in self.overlaped_points.values():
            if nb_overlap > 1:
                sum += 1
        return sum


# init segments
segments = []
with open("input.txt", "r") as vents_file:
    for line in [line.strip() for line in vents_file]:
        p1, p2 = line.split(" -> ")
        p1 = Point(*map(int, p1.split(",")))
        p2 = Point(*map(int, p2.split(",")))
        segments.append(Segment(p1, p2))


grid = Grid(segments)
grid.generate_overlaped_points()
print(grid.sum_overlaped_points())
