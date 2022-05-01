#
# Author: yilmazturkm
# Author Github: https://github.com/yilmazturkm
# Author Url: https://yilmazturk.gen.tr
#
# This script is a python input and list example
# It asks user to input a number and it compare the number with the numbers in the given list.
# Then it prints out the smaller numbers than entered number.
#

# Ask user to input a number
num = int(input("Enter the number: "))

#Create a list
a = [0,1,2,3,5,8,13,21,34,55,89]

# Create an empty list
b = []

# For loop to compare the number and list
for i in a:
    if i < num: # if number of the list is lower than entered number
        b.append(i) # add it to list b

# Print the list b
print(b)