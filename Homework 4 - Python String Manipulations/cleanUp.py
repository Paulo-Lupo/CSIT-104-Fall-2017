# Homework 4 - cleanUp.py			#
# Student Name: Joao Paulo Dos Santos Ferreira	#
# CSIT 104-03 - Computational Concepts		#
# Dr. Bharath Kumar Samanthula			#
# November 26, 2017				#

# This program gets an input from the user		#
# -Removes all vowels					#
# -Replaces all v's with b's and all b's with v's	#
# -Counts the number of letters in the new sentence	#

# Reads the input from the user
s = input("Enter a sentence: ")

# Remove all vowels
nv = ''
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
for letter in s:
    if letter in vowels:
        nv = nv
    else:
        nv = nv + letter
print("Phrase with no vowels: " + nv)

# Replaces all v and b in the original sentence with b and v, respectively
S = ''
for letter in s:
    if letter == 'v':
        S = S + 'b'
    elif letter == 'b':
        S = S + 'v'
    else:
        S = S + letter

# Counts the number of letters in the modified sentence
count = 0
for letter in s:
    if letter == ' ':
        count = count + 0
    else:
        count = count + 1

# Prints the resulting sentence and the number of letters in that sentence
print("Modified sentence with v and b replaced with b and v, respectively = " + S)
print("Number of letters in the modified sentence = " + str(count))
