# Homework 5 - isOdd.py				#
# Student Name: Joao Paulo Dos Santos Ferreira	#
# CSIT 104-03 - Computational Concepts		#
# Dr. Bharath Kumar Samanthula			#
# December 5, 2017				#

# This program tells the user if the number	#
# entered is odd or even			#

# Reads the input from the user
n = int(input("Enter an integer number: "))

# Checks if the number is odd or even
if (n % 2) == 0:
    print("The number is even!")
else:
    print("The number is odd!")
