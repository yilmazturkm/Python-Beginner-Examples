#
# Author: yilmazturkm
# Author Github: https://github.com/yilmazturkm
# Author Url: https://yilmazturk.gen.tr
# 
# Check if a number is prime.
# it asks user to input a number and check if the number is prime or not.
#


# Create a function to determine number is prime or not
def isPrime(num):
    result = None
    if num == 2:
        result = False
    elif num < 2:
        result = False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
            else:
                result = True
    return result

# Create a function to get input from user
def getInputandCheck():
    while True:
        number = input("Tyep a number (q for exit): ")
        if number.lower() == "q":
            break
        else:
            try:
                number = int(number)
                if isPrime(number):
                    print(f"{number} is prime")
                else:
                    print(f"{number} is not prime")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    getInputandCheck()
            