"""
George Athanasopoulos
Feb 10, 2026
Lab 6, Classes Object, and Methods
"""



print("\n ----- Example 1: Classes -----")
# A class is like a blueprint of something
# Using the class, we can create different instance of an object
# Data attributes (properties) are values that represent an object
# Methods are functions of an object

class Circle(object):
    def __init__(self, radius, color):
        self.r = radius
        self.c = color
    
    # Method to add value to the radius
    def add_radius(self, plusradius):
        self.r += plusradius
        return self.r

class Rectangle(object):
    def __init__(self, height, width, color):
        self.h = height
        self.w = width
        self.c = color
    
    # Method to calculate and return the area of the rectangle
    def area(self):
        return self.h * self.w
    
    # Method to calculate and return the perimeter of the rectangle
    def perimeter(self):
        return (2*self.w) + (2*self.h)
    
    # Method to draw the rectangle
    def draw_rectangle(self):
        plt.gca().ad_patch(plt.Rectangle((0,0), self.w, self.h, fc=self.c))
        plt.axis("scaled")
        plt.show()

# Create an instance of an object
circle1 = Circle(5, "yellow")
circle2 = Circle(2, "red")
rectangle1 = Rectangle(2, 3, "green")
rectangle2 = Rectangle(5, 4, "blue")

# Accessing to data in an object
print(f"Color of circle 2 is: {circle2.c}")
print(f"The area of rectangle 1 is: {rectangle1.w * rectangle1.h}")
print(f"The area of rectangle 1 is: {rectangle2.w * rectangle2.h}")

# Modify data of an object
circle2.c = "orange"
print(f"Color of circle 2 after modification = {circle2.c}")

# Call method add_radius in circle2 an pass 6
print(f"Radius of circle 2 before method add_radius = {circle2.r}")
circle2.add_radius(6)
print(f"Radius of circle 2 after method add_radius = {circle2.r}")

# Call methods in class Rectangle
print(f"The area of rectangle 1 = {rectangle1.area()}")
print(f"The perimeter of rectangle 2 = {rectangle2.perimeter()}")

# Draw rectangle
# rectangle2.draw_rectangle()       (MODULE NOT IMPORTED ON CODESPACE)


print("\n ----- EXERCISE -----")
class BankAccount:
    def __init__(self, account_number, account_holder, balance = 250.50):
        self.n = account_number
        self.h = account_holder
        self.b = balance

    def deposit(self, amount):
        self.b += amount
        print(f"${amount} deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.b:
            self.b -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient balance. Withdrawal cannot be made.")

    def balance(self):
        print(f"Final balance $ {self.b}")

useraccount = BankAccount(123456789, "George Athanasopoulos")

useraccount.withdraw(700)
useraccount.deposit(1000)
useraccount.withdraw(500)
useraccount.balance()