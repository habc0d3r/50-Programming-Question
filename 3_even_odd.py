# Write a program to check if a number is even or odd.

def is_even(a):
    if type(a) != int:
        return "Input must be an integer"
    if a % 2 == 0:
        flag = True
    else:
        flag = False
    return flag


print(is_even(0))
print(is_even(6))
print(is_even(-9))