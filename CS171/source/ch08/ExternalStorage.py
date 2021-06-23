#!/usr/bin/env python3
# Copyright (c) 2008-11 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version. It is provided for educational
# purposes and is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

"""
This module provides the Point and Circle classes with all data held
separately in the ExternalStorage class.

>>> point = Point()
>>> point
Point(0, 0)
>>> point.x = 12
>>> str(point)
'(12, 0)'
>>> a = Point(3, 4)
>>> b = Point(3, 4)
>>> a == b
True
>>> a == point
False
>>> a != point
True

>>> circle = Circle(2)
>>> circle
Circle(2, 0, 0)
>>> circle.radius = 3
>>> circle.x = 12
>>> circle
Circle(3, 12, 0)
>>> a = Circle(4, 5, 6)
>>> b = Circle(4, 5, 6)
>>> a == b
True
>>> a == circle
False
>>> a != circle
True
>>> circle.X
Traceback (most recent call last):
    ...
AttributeError: 'Circle' object has no attribute 'X'
"""

import math


class ExternalStorage:

    __slots__ = ("attribute_name",)
    __storage = {}


    def __init__(self, attribute_name):
        self.attribute_name = attribute_name


    def __set__(self, instance, value):
        self.__storage[id(instance), self.attribute_name] = value


    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        return self.__storage[id(instance), self.attribute_name]


class Point:

    __slots__ = ()
    x = ExternalStorage("x")
    y = ExternalStorage("y")

    def __init__(self, x=0, y=0):
        """A 2D cartesian coordinate

        >>> point = Point()
        >>> point
        Point(0, 0)
        """
        self.x = x
        self.y = y


    @property
    def distance_from_origin(self):
        """Returns the distance of the point from the origin

        >>> point = Point(3, 4)
        >>> point.distance_from_origin
        5.0
        """
        return math.hypot(self.x, self.y)


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


    def __repr__(self):
        return "Point({0.x!r}, {0.y!r})".format(self)


    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)



class Circle(Point):

    __slots__ = ()
    __radius = ExternalStorage("__radius")

    def __init__(self, radius, x=0, y=0):
        """A Circle

        >>> circle = Circle(2)
        >>> circle
        Circle(2, 0, 0)
        >>> circle.radius, circle.x, circle.y
        (2, 0, 0)
        """
        super().__init__(x, y)
        self.radius = radius


    @property
    def area(self):
        """The circle's area

        >>> circle = Circle(3)
        >>> a = circle.area
        >>> int(a)
        28
        """
        return math.pi * (self.radius ** 2)


    @property
    def edge_distance_from_origin(self):
        """The distance of the circle's edge from the origin

        >>> circle = Circle(2, 3, 4)
        >>> circle.edge_distance_from_origin
        3.0
        """
        return abs(self.distance_from_origin - self.radius)


    @property
    def circumference(self):
        """The circle's circumference

        >>> circle = Circle(3)
        >>> d = circle.circumference
        >>> int(d)
        18
        """
        return 2 * math.pi * self.radius


    @property
    def radius(self):
        """The circle's radius

        >>> circle = Circle(-2)
        Traceback (most recent call last):
        ...
        AssertionError: radius must be nonzero and non-negative
        >>> circle = Circle(4)
        >>> circle.radius = -1
        Traceback (most recent call last):
        ...
        AssertionError: radius must be nonzero and non-negative
        >>> circle.radius = 6
        """
        return self.__radius

    @radius.setter
    def radius(self, radius):
        assert radius > 0, "radius must be nonzero and non-negative"
        self.__radius = radius


    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)


    def __repr__(self):
        return ("{0.__class__.__name__}({0.radius!r}, {0.x!r}, "
                "{0.y!r})".format(self))


if __name__ == "__main__":
    import doctest
    doctest.testmod()

