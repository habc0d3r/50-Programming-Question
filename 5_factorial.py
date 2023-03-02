# Write a program to find the factorial of a number.
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        try:
            result *= i
        except OverflowError:
            print("Factorial of %d is too large to compute." % n)
            return None
    return result

