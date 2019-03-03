# Homework 5 - countdice.py			#
# Student Name: Joao Paulo Dos Santos Ferreira	#
# CSIT 104-03 - Computational Concepts		#
# Dr. Bharath Kumar Samanthula			#
# December 5, 2017				#

# This program computes the rolling of a die 50 times
# Shows the average between the rolls and the most frequent roll

# Imports the random package to be used to roll the die
import random

# Assigns min and max values for the dice rolls, and the sum of those values
min = 1
max = 6
sum = 0

# Initializes an array to store the amount of times each side rolled
count = [0, 0, 0, 0, 0, 0]

# Initializes an array to store all the dice rolls
dice = [random.randint(min, max) for i in range(50)]

# Loop to count the frequency of each side of the die, and the sum of those values
for i in range(50):
    if dice[i] == 1:
        count[0] = count[0] + 1

    elif dice[i] == 2:
        count[1] = count[1] + 1

    elif dice[i] == 3:
        count[2] = count[2] + 1

    elif dice[i] == 4:
        count[3] = count[3] + 1

    elif dice[i] == 5:
        count[4] = count[4] + 1

    elif dice[i] == 6:
        count[5] = count[5] + 1

    sum = sum + dice[i]

# Sorts the most frequent side of the die
freqNum = 1
freq = 0
for i in range(6):
    if count[i] > freq:
        freq = count[i]

# Calculates the average die value of all rolls
avr = sum/50

# Prints the frequency of each die
print("# of times 1 was rolled: " + str(count[0]))
print("# of times 2 was rolled: " + str(count[1]))
print("# of times 3 was rolled: " + str(count[2]))
print("# of times 4 was rolled: " + str(count[3]))
print("# of times 5 was rolled: " + str(count[4]))
print("# of times 6 was rolled: " + str(count[5]))

# Prints the results
print("The most frequent side of the die was: ")
for i in range(6):
    if count[i] == freq:
        print(i+1)
print("The average die value of rolls is: " + str(avr))
