# Homework 4 - counting.py			#
# Student Name: Joao Paulo Dos Santos Ferreira	#
# CSIT 104-03 - Computational Concepts		#
# Dr. Bharath Kumar Samanthula			#
# November 26, 2017				#

# This program gets an input from the user	#
# -Counts the number of characters and words	#
# -Counts the number of vowels in the sentence	#

# Reads the input from the user
q = input("Enter a sentence: ")

# Counts the number of words
w = len(q.split())
print("Number of words in the sentence = " + str(w))

# Counts the number characters and symbols that are not space
c = q.count(" ")
l = len(q)
print("Number of words and characters not included space = " + str(l-c))

# Counts the number of vowels
q = q.lower()
a = q.count('a')
e = q.count('e')
i = q.count('i')
o = q.count('o')
u = q.count('u')
print("Number of vowels in the sentence = " + str(a+e+i+o+u))
