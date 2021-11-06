import unittest
from main import *
import random
import operator
import math

SEED = 1234


class PathsData:
    square_points = None
    square_time = None
    square_required = None

    random_points = None
    random_time = None
    random_required = None

    efficient_points = None
    efficient_time = None
    efficient_required = None

    worst_points = None
    worst_time = None
    worst_required = None

    def create_paths_data(self):
        self.efficient_points = [
            Vector(0, 0),
            Vector(1, 1),
            Vector(2, 2),
        ]
        self.efficient_time = [1] * (len(self.efficient_points) - 1)
        self.efficient_required = [1]

        self.square_points = [
            Vector(0, 0),
            Vector(0, 1),
            Vector(1, 1),
            Vector(1, 0)
        ]
        self.square_time = [1] * (len(self.square_points) - 1)
        self.square_required = [1]

        self.random_points = [Vector(random.random() * random.randint(1, 10), random.random() * random.randint(1, 10))
                              for _ in range(100)]
        self.random_time = [random.random() for _ in range(len(self.random_points) - 1)]
        self.random_required = list(sorted({random.randint(1, 98) for _ in range(10)}))

        self.worst_points = [Vector(0, 0), Vector(math.inf, math.inf), Vector(0, 0)]
        self.worst_time = [math.inf] * 2
        self.random_required = []


class TestVector(unittest.TestCase):
    def setUp(self) -> None:
        random.seed(SEED)

    def test_defaults_zero(self):
        zero_vector = Vector()

        self.assertIsInstance(zero_vector, Vector)
        self.assertEqual(0, zero_vector.x)
        self.assertEqual(0, zero_vector.y)

    def test_creation(self):
        x, y = random.random(), random.random()

        vector = Vector(x, y)

        self.assertIsInstance(vector, Vector)
        self.assertEqual(x, vector.x)
        self.assertEqual(y, vector.y)

    def test_length_egypt(self):
        self.assertEqual(5, abs(Vector(3, 4)))

    def test_length(self):
        x, y = random.random(), random.random()

        vector = Vector(x, y)

        self.assertEqual((x ** 2 + y ** 2) ** .5, abs(vector))

    def test_eq(self):
        self.assertEqual(Vector(), Vector())

    def test_addition(self):
        left = Vector()
        x, y = random.random(), random.random()
        right = Vector(x, y)

        self.assertIsInstance(left + right, Vector)
        self.assertEqual(Vector(x, y), right)

        self.assertRaises(TypeError, operator.add, left, 0)

    def test_multiplex(self):
        x, y = random.random(), random.random()
        left = Vector(x, y)
        right = random.random()

        self.assertIsInstance(left * right, Vector)

        self.assertEqual(left * right, Vector(x * right, y * right))

        self.assertRaises(TypeError, operator.mul, left, left)

    def test_into_tuple(self):
        vector = Vector()
        tuple_vector = tuple(vector)

        self.assertIsInstance(tuple_vector, tuple)
        self.assertEqual((0, 0), tuple_vector)


class TestPath(unittest.TestCase, PathsData):
    def setUp(self) -> None:
        random.seed(SEED)

        self.create_paths_data()

    def test_creation(self):
        path = Path(self.square_points, self.square_time, self.square_required)

        self.assertIsInstance(path, Path)
        self.assertEqual(self.square_points, path.points)
        self.assertEqual(self.random_time, path.time_between_points)

    def test_kpd(self):
        path = Path(self.square_points, self.square_time, self.square_required)

        kpd = path.kpd()

        self.assertLess(1, kpd)
        self.assertLess(kpd, 0)

        efficient_path = Path(self.efficient_points, self.efficient_time, self.efficient_required)

        self.assertEqual(1, efficient_path.kpd())


class TestCompany(unittest.TestCase, PathsData):
    def setUp(self) -> None:
        random.seed(SEED)

        self.create_paths_data()

        self.efficient_path = Path(self.efficient_points, self.efficient_time, self.efficient_required)
        self.random_path = Path(self.random_points, self.random_time, self.random_required)
        self.square_path = Path(self.square_points, self.square_time, self.square_required)
        self.worst_path = Path(self.worst_points, self.worst_time, self.worst_required)
        self.paths = [self.square_path, self.random_path, self.efficient_path, self.worst_path]

    def test_creation(self):
        company = Company(self.paths)

        self.assertIsInstance(company, Company)
        self.assertEqual(self.paths, company.paths)

    def test_best_path(self):
        company = Company(self.paths)

        self.assertEqual(self.efficient_path, company.best_path)

    def test_worst_path(self):
        company = Company(self.paths)

        self.assertEqual(self.worst_path, company.worst_path)
