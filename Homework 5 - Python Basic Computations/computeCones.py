# Homework 5 - computeCones.py			#
# Student Name: Joao Paulo Dos Santos Ferreira	#
# CSIT 104-03 - Computational Concepts		#
# Dr. Bharath Kumar Samanthula			#
# December 5, 2017				#

# This program computes the surface area and 	#
# volume of a cone based on the user's input	#

# Imports the math package
import math

# Prints a message indicating what the program does
print("The following program calculates the surface area and volume of a cone")

# Scans the user input and initializes the variables
r = float(input("Enter the radius of the cone in feet(non-negative float value): "))
h = float(input("Enter the height of the cone in feet(non-negative float value): "))

# Rounds the variables to two decimal digits and prints them
print("Radius rounded to two decimal digts: " + str(round(r,2)))
print("Height rounded to two decimal digts: " + str(round(h,2)))

# Defines the function to calculate the surface area of a cone
def cone_surface_area(r, h):
    a = math.pi*(r*r + r*math.sqrt(r*r+h*h))
    return a;

# Defnines the function to calculate the volume of a cone
def cone_volume(r, h):
    v = math.pi*r*r*h/3
    return v;

# Invokes the functions created and print the resuts rounded to two decimal digts
a = cone_surface_area(r, h)
print("The surface area of the cone (rounded to two decimal digits) is: " + str(round(a,2)))
v = cone_volume(r, h)
print("The volume of the cone(rounded to two decimal digits) is: " + str(round(v,2)))
