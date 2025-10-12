# polymorphism_demo.py

import math

# Base Class
class Shape:
    def area(self):
        """Method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement the area() method.")


# Derived Class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override area method to calculate rectangle area."""
        return self.length * self.width


# Derived Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Override area method to calculate circle area."""
        return math.pi * (self.radius ** 2)

