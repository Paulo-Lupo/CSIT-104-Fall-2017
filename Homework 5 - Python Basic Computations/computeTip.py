# Homework 5 - computeTip.py			#
# Student Name: Joao Paulo Dos Santos Ferreira	#
# CSIT 104-03 - Computational Concepts		#
# Dr. Bharath Kumar Samanthula			#
# December 5, 2017				#

# This program gets an number for the user	#
# -Computes how much 15% and 20% tip		#
# on the total bill should be			#

# Reads the input from the user
b = float(input("Enter the bill amount: "))

# Outputs two options for tipping
t15 = 0.15*b
t20 = 0.20*b
print("Options for tipping: ")
print(" 15% = $" + str(t15))
print(" 20% = $" + str(t20))
