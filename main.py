from dataclasses import dataclass, field


@dataclass
class Vector:
    x: float = field(default=0)
    y: float = field(default=0)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __mul__(self, multiplier: float):
        return Vector(self.x * multiplier, self.y * multiplier)

    def __add__(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y)

    def length(self):
        return (self.x ** 2 + self.y ** 2) ** .5

    def __abs__(self):
        return self.length()


@dataclass
class Path:
    points: list[Vector] = field(default_factory=list)
    time_between_points: list[float] = field(default_factory=list)

    def kpd(self, required_indexes: list[int] = []):
        return self.minimal_distance(required_indexes) / self.current_distance()

    def current_distance(self) -> float:
        return sum(abs(self.points[i + 1] - self.points[i]) / self.time_between_points[i] for i in range(len(self.points) - 1))

    def minimal_distance(self, required_indexes: list[int] = []) -> float:
        new_points = [self.points[0], self.points[-1]]
        for index, i in enumerate(required_indexes):
            new_points.insert(index + 1, self.points[i])
        return sum(abs(new_points[i + 1] - new_points[i]) / self.time_between_points[i] for i in range(len(new_points) - 1))


@dataclass
class Company:
    paths: list[Path] = field(default_factory=list)


if __name__ == '__main__':
    path = Path([Vector(0, 0),
                 Vector(0, 1),
                 Vector(1, 1),
                 Vector(1, 0)],
                [1, 2, 3])
    print(path.kpd([1]))
