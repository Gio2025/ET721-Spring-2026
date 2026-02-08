"""
George Athanasopoulos
Feb 5, 2026
Lab 5, Functions
"""

from Lab5_function_Athanasopoulos import *
import math

print("\n----- Example 1: User-defined function -----")
w = 10
l = 2
a = area_rectangle(w,l)
# print(f"The area of the rectangle of {w} and {l} is {a}")
print_area_result(w, l, a)


print("\n----- Example 2: Calculate the distance of two points -----")
x1 = collectnum('x1')
x2 = collectnum('x2')
y1 = collectnum('y1')
y2 = collectnum('y2')

# testing
# print(f"({x1},{y1}) ({x2},{y2})")

# testing
# print(f"Distance = {calculate_distance(x1,x2,y1,y2)}")

GUESS_NUMBER = 7

random_number = generate_random(1, 10)
compare_with_guess(random_number, GUESS_NUMBER)