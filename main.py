from dataclasses import dataclass, field


@dataclass
class Vector:
    x: float = field(default=0)
    y: float = field(default=0)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __mul__(self, multiplier: float):
        x = self.x * multiplier
        y = self.y * multiplier
        return Vector(x, y)

    def __add__(self, vector):
        x = self.x + vector.x
        y = self.y + vector.y
        return Vector(x, y)

    def __sub__(self, vector):
        x = self.x - vector.x
        y = self.y - vector.y
        return Vector(x, y)

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** .5


@dataclass
class Path:
    points: list[Vector] = field(default_factory=list)

    def kpd(self, required_indexes: list[int] = []):
        return self.minimal_distance(required_indexes) \
               / self.current_distance()

    def current_distance(self) -> float:
        length = 0.0
        for i in range(len(self.points) - 1):
            length += (self.points[i + 1] - self.points[i]).length()
        return length

    def minimal_distance(self, required_indexes: list[int] = []) -> float:
        new_points, length = [self.points[0], self.points[-1]], 0.0
        for index, i in enumerate(required_indexes):
            new_points.insert(index + 1, self.points[i])
        for i in range(len(new_points) - 1):
            length += (new_points[i + 1] - new_points[i]).length()
        return length


@dataclass
class Company:
    paths: list[Path] = field(default_factory=list)


if __name__ == '__main__':
    path = Path([Vector(0, 0),
                 Vector(0, 1),
                 Vector(1, 1),
                 Vector(1, 0)])
    print(path.kpd())
