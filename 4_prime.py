# Write a program to check if a number is prime or not.
def is_prime(num):
    if num <= 1:
        return "Not Prime"
    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            return "Not Prime"
    return "Prime"
