# Write a program to find the sum of two numbers.

# Defining a function named print_sum with two parameters a and b
def print_sum(a, b):
    # starting exception handling for possible exceptions
    try:
        # type casting a and b to int and
        # storing the value of a + b in result variable
        result = int(a) + int(b)
        # returning the result
        return result
    except Exception as e:
        return e


# print(print_sum(8, 5))
# print(print_sum(a=input('a: '), b=input('b: ')))

