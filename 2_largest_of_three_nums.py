# Write a program to find the largest among three numbers.

# Define a function called find_largest with 3 parameter
def find_largest(a, b, c):
    # using exception handling
    try:
        if a > b and a > c:
            largest = a
        elif b > a and b > c:
            largest = b
        else:
            largest = c
        return largest
    except Exception as e:
        return "There's an issue here!", e


# print(find_largest('d', 3, 5))
# print(find_largest(43, 64, 15))
