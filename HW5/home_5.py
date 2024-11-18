# reate an abstract class-interface Volumetric containing the definition of the property-method volume.
from abc import abstractmethod
from abc import ABCMeta

class Volumetric(metaclass=ABCMeta):

    @abstractmethod
    def volume(self):
        raise NotImplementedError

# Create an Area interface class describing all classes that can have an area.
# Define the signature of the area() property-method in the class similarly to volume() in the previous tasks.

class Area (metaclass=ABCMeta):

    @abstractmethod
    def area(self):
        raise NotImplementedError

# Add a basic abstract class Shape2D as a descendant of the class Area.
# Define comparison operators in the class, using area values for this purpose (calling property-method area).

class Shape2D(Area, metaclass=ABCMeta):
# --would make the class abstract at least one abstract method:
    @abstractmethod
    def area(self):
        raise NotImplementedError

# ----- < is the opposite of ≥,
# ----- > is the opposite of ≤,
# ---- == is the opposite of !=

    def __lt__(self, other):  # x < y
        return self.area < other.area

    def __ge__(self, other):  # x ≥ y
        return not (self < other)

    def __gt__(self, other):  # x > y
        return self.area > other.area

    def __le__(self, other):  # x ≤ y
        return not (self > other)

    def __eq__(self, other):  # x == y
        return self.area == other.area

    def __ne__(self, other):  # x != y
        return not (self == other)


#Create a basic abstract Shape3D class that inherits from Volumetric.
# Make the Shape3D class inherit from Volumetric and Area classes simultaneously.

class Shape3D(Volumetric, Area, metaclass=ABCMeta):

    @abstractmethod
    def volume(self):
        raise NotImplementedError

# This class contains the implementation of comparison operators from Parallelepiped.
# It is necessary to make it possible to compare objects of the class using operators: >, <, >=, <=, ==, !=.
# Comparison is done by comparing parallelepiped volumes.

    def __lt__(self, other):  # x < y
        return self.volume < other.volume

    def __ge__(self, other):  # x ≥ y
        return not (self < other)

    def __gt__(self, other):  # x > y
        return self.volume > other.volume

    def __le__(self, other):  # x ≤ y
        return not (self > other)

    def __eq__(self, other):  # x == y
        return self.volume == other.volume

    def __ne__(self, other):  # x != y
        return not (self == other)


# Create a Parallelepiped class with three fields: length, width, height.
# .Inherit the Parallelepiped class from Shape3D.

class Parallelepiped(Shape3D):
    length: float
    width: float
    height: float

    def __init__ (self, l, w, h):
        if isinstance(l, (float, int)):
           self.length = l
        else:
           raise ValueError(f"length expected to be float or int, {type(l)} found")
        if isinstance(w, (float, int)):
           self.width = w
        else:
           raise ValueError(f"width expected to be float or int, {type(w)} found")
        if isinstance(h, (float, int)):
           self.height = h
        else:
           raise ValueError(f"height expected to be float or int, {type(h)} found")

# Make the volume calculation functionality a separate property-method volume.
    @property
    def volume(self):
        return self.height * self.width * self.length


# Implement the __str__ method that turns an object into a string of the form: “Parallelepiped (1x2x3)”,

    def __str__(self):
        return (f"Parallelepiped ({self.length}x{self.width}x{self.height})")

#  In the Parallelepiped class, implement the area method using the formula: S = 2(ab + bc + ac)
    @property
    def area(self):
        return 2*(self.width*self.length + self.length*self.height + self.width*self.height)

a = Parallelepiped(1, 2.9, 3)
b = Parallelepiped(1, 2, 4)
print("Parallelepiped")
print(f"V(b) =  {b.volume}")
print(f"V(a) =  {a.volume}")
print(f"a<b is {a<b}")
print(f"a>=b is {a>=b}")
print(f"str method for b =  {b}")
print(f"S (a) = {a.area}")


# Add a Sphere class that inherits from Shape3D.
# When calculating the volume, we need the radius parameter, which is the only parameter passed to the constructor.
# V = 4/3 * pi * R**3 ,
# where R is the radius, pi is the constant math.pi from the module math.

from math import pi, sin

class Sphere (Shape3D):
    radius:float

    def __init__(self,r):
        if isinstance(r, (float, int)):
            self.radius = r
        else:
           raise ValueError(f"radius to be float or int, {type(r)} found")


    @property
    def volume(self):
        return 4/3*pi*self.radius**3

# Implement the area method for the Sphere class using the formula: S = 4*pi*R*R
    @property
    def area(self):
        return 4*pi*self.radius*self.radius

Sph1 = Sphere(2)
Sph2 = Sphere(5)

print("\nSphere")
print(f"V(Sph1) =  {Sph1 .volume}")
print(f"V(Sph2) =  {Sph2.volume}")
print(f"Sph2 = Sph1 is {Sph2 == Sph1 }")
print(f"Sph2 != Sph1 is {Sph2 != Sph1 }")
print(f"S (Sph1) = {Sph1.area}")


# Create a Parallelogram class that inherits from Shape2D. Implement the area method using the formula:
# S = a * b * sinA, where
# a, b - sides (passed to the constructor),
# A - angle between sides a and b, given in degrees. The sine is calculated as follows:
# sinA = math.sin(A*math.pi / 180)
class Parallelogram(Shape2D):
    a:float
    b:float
    A:float

    def __init__(self,a,b,A):
        if isinstance(a, (float, int)):
            self.a = a
        else:
           raise ValueError(f"a to be float or int, {type(a)} found")
        if isinstance(b, (float, int)):
            self.b = b
        else:
           raise ValueError(f"b to be float or int, {type(b)} found")
        if isinstance(A, (float, int)):
            self.A = A
        else:
           raise ValueError(f"radius to be float or int, {type(A)} found")


# the conversion of degrees to radians using the static method of the Parallelogram class.
    @staticmethod
    def sin_change(A):
        return sin(A * pi / 180)

    @property
    def area(self):
        return self.a*self.b*self.sin_change(self.A)

pr1 = Parallelogram(3,4, 60)
pr2 = Parallelogram(5,6, 30)
print("\nParallelogram")
print(f"pr2 = pr1 is {pr2 > pr1 }")
print(f"pr2 != pr1 is {pr2 <= pr1 }")
print(f"S (pr2) = {pr2.area}")
