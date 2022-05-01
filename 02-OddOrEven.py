#
# Author: yilmazturkm
# Author Github: https://github.com/yilmazturkm
# Author Url: https://yilmazturk.gen.tr
#
# This script is an example for finding if a number is even or odd
# It asks user to input a number to check if it is even or odd
# Also it asks user to input another number to check if the the number is multiplier of the first number
#

# Ask user to input a number and assign it to num1 variable
num1 = int(input("Enter a number: "))

# Ask user to input another number and assign it to num2 variable
num2 = int(input("Enter another number: "))

# if else statement to check if num1 is even or odd
if num % 2 == 0: # num1 is even
    print(f"{num} is even") # print message
else: # num1 is odd
    print(f"{num} is odd") # print message
    
# if statement to check if num1 is mulpilier of num2
if num % check == 0:
    print(f"{check} divides evenly into {num}")