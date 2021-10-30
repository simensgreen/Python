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

    def kpd(self):
        return self.minimal_distance() / self.distance(self.points)

    @staticmethod
    def distance(points: list[Vector]) -> float:
        length = 0.0
        for i in range(len(points) - 1):
            length += (points[i + 1] - points[i]).length()
        return length

    def distance_with_required_points(self,
                                      required_indexes: list[int]) -> float:
        new_points, length = [self.points[0], self.points[-1]], 0.0
        for index, i in enumerate(required_indexes):
            new_points.insert(index + 1, self.points[i])
        return self.distance(new_points)

    def minimal_distance(self) -> float:
        return (self.points[-1] - self.points[0]).length()


@dataclass
class Company:
    paths: list[Path] = field(default_factory=list)


if __name__ == '__main__':
    path = Path([Vector(0, 0),
                 Vector(0, 1),
                 Vector(1, 1),
                 Vector(1, 0)])
    print(path.minimal_distance())
    print(path.distance(path.points))
    print(path.distance_with_required_points([0, 1]))
