from __future__ import annotations
import math


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError

    def __sub__(self, other: Vector) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        raise TypeError

    def __mul__(self, other: Vector | int | float) -> Vector | int | float:
        if isinstance(other, Vector):
            scalar = self.x * other.x + self.y * other.y
            return scalar
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        raise TypeError

    @classmethod
    def create_vector_by_two_points(
        cls, start_point: tuple, end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return math.sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cos_a = (self * other) / (self.get_length() * other.get_length())
        return int(round(math.degrees(math.acos(cos_a)), 0))

    def get_angle(self) -> int:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        sin = math.sin(math.radians(degrees))
        cos = math.cos(math.radians(degrees))
        rotate_x = self.x * cos - self.y * sin
        rotate_y = self.x * sin + self.y * cos

        return Vector(rotate_x, rotate_y)
