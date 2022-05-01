#
# Author: yilmazturkm
# Author Github: https://github.com/yilmazturkm
# Author Url: https://yilmazturk.gen.tr
#
# A python overlap script example.
# It creates two random list. Than it comparet these two list and get the overlap elements of the lists
#


# Import random module
import random

# Create two empty lists
a = []
b = []

# Fill the lists with random 20 elements
for i in range(20):
    a.append(random.randint(0, 100))
    b.append(random.randint(0, 100))
    
# Print the lists
print(f"List a: {a}")
print(f"List b: {b}")

# Create an empty list
commons = []

# For loop to find the overlap
for i in a:
    if i in b:
        commons.append(i)

# Print common elements (use set function to eleminate same elements)
print(list(set(commons)))