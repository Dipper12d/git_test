# define functions
import math


def disprect(length, width):
    area = length * width
    print(f"The area of the rectangle is {area:.2f} ")


def disptri(base, height):
    triarea = 0.5 * base * height
    print(f"The area of the triangle is {triarea:.2f}")


def dispcir(radius):
    circarea = math.pi * radius * radius
    print(f"The area of circle is {circarea:.2f}")


disprect(11.5, 2.75)
disptri(8.5, 7.5)
dispcir(9.6)
