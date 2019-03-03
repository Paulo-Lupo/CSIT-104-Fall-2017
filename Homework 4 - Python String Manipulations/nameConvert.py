# Homework 4 - nameConvert.py			#
# Student Name: Joao Paulo Dos Santos Ferreira	#
# CSIT 104-03 - Computational Concepts		#
# Dr. Bharath Kumar Samanthula			#
# November 26, 2017				#

# This program gets an input from the user		#
# -Prints the sentence in lower case			#
# -Prints the sentence with the vowels in upper case	#
# and consonants in lower case				#
# -Writes the sentence in reverse order			#

# Reads the input from the user
S = input("Enter a sentence: ")

# Writes the sentence in all lower case
s = S.lower()
print("phrase converted to lower case: " + s)

# Writes the sentence with all consonants in lower case and all vowels in upper case
s = s.replace('a', 'A')
s = s.replace('e', 'E')
s = s.replace('i', 'I')
s = s.replace('o', 'O')
s = s.replace('u', 'U')
print("phrase with vowels in uppercase and consonant and lower case: " + s)

# Writes the original sentence in reverse order
r = S[::-1]
print("phrase in the reverse order: " + r)
