#
# Author: yilmazturkm
# Author Github: https://github.com/yilmazturkm
# Author Url: https://yilmazturk.gen.tr
#
# This script is an example of Python Character Input
# It asks user to type their name and current age and calculate the year when user is 100 years old.
#

#Import datetime module
from datetime import datetime

#Get current year and assign it to thisYear variable
thisYear = datetime.today().year

#Get name and age from user
name = input("Your Name: ")
age = int(input("Your Age: "))

#Get number of message user wants to print on the screen
numberOfMessage = int(input("How many message print you want!: "))

#Calculate the year
remainingYear = 100 - age
targetYear = thisYear + remainingYear

#Print the message
print(f"{name}, you'll be 100 years old in {targetYear} \n" * numberOfMessage)