#
# Author: yilmazturkm
# Author Github: https://github.com/yilmazturkm
# Author Url: https://yilmazturk.gen.tr
#
# Python script to find divisors of a number.
# It asks user to input a number, finds its divisors and print the divisors of the number
#

# Get a number from the user and assign it to num variable
num = int(input("Enter number to find divisors: "))

# Create an empty list
divisorList = []

# For loop to iterate all number from 1 to num
for i in range(1, num):
    if num % i == 0: # if i is a divisor of num
        divisorList.append(i) # add i to divisorList

# Print divisorList
print(divisorList)