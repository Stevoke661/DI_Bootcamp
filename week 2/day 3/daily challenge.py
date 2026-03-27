#challenge 1
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2

    @classmethod
    def from_diameter(cls, diameter):
        """Allows creating a circle using Circle.from_diameter(10)"""
        return cls(diameter / 2)

    @property
    def area(self):
        """Computes area: A = πr²"""
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area:.2f})"

    def __repr__(self):
        return f"Circle({self.radius})"

    def __add__(self, other):
        """Adds two circles and returns a new Circle instance."""
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        """Checks if this circle is larger than another."""
        return self.radius > other.radius

    def __lt__(self, other):
        """Necessary for sorting."""
        return self.radius < other.radius

    def __eq__(self, other):
        """Checks if two circles have the same radius."""
        return self.radius == other.radius

# --- Testing the Implementation ---

c1 = Circle(5)
c2 = Circle.from_diameter(20)
c3 = Circle(2)

circles = [c1, c2, c3]

print(f"Circle 1: {c1}")
print(f"Circle 2 Area: {c2.area:.2f}")
print(f"Is C2 > C1? {c2 > c1}")

c4 = c1 + c3
print(f"New Circle (C1 + C3): {c4}")

print("\nSorted Circles:")
for c in sorted(circles):
    print(c)