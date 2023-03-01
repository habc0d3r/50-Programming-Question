# Write a program to check if a number is prime or not.
def is_prime(num):
    for i in range(2, num-1):
        if num % i == 0:
            return "Not Prime"
    return "Prime"



