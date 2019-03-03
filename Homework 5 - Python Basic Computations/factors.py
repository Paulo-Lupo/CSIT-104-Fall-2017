# Homework 5 - factors.py			#
# Student Name: Joao Paulo Dos Santos Ferreira	#
# CSIT 104-03 - Computational Concepts		#
# Dr. Bharath Kumar Samanthula			#
# December 5, 2017				#

# This program computres the factors	#
# of a positive integer number		#

# Gets the output from the user
n = int(input("Enter a positive integer value: "))

# Checks if the number is positive, negative and different than 0.
if (n > 0):
	# Initializes an array to store which numbers are factors of the number given by the user
	factors = [0 for i in range(n+1)]

	# Checks which numbers are factors of the given number and assigns them to the array
	for i in range(n+1):
		if(i == 0):
			factors[i] = i
		elif(n % i == 0):
			factors[i] = i
			
	# Prints the results
	print("All of the factors of " + str(n) + " are: ", end = '')
	for i in range(n+1):
		if(factors[i] != 0 and factors[i] != n):
			print(factors[i], end=', ')
		elif factors[i] == n:
			print(factors[n], end ='.')
			
# Exception checks
elif(n < 0):
	print("You cannot enter a negative value.")
else:
	print("0 has no factors.")
