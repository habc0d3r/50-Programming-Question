# Write a program to calculate the area of a circle.
# Make it a generally usable function to find area of circle
def find_area(r):
    if int(r) <= -1:
        return "Radius cannot be negative. Retry!"
    try:
        area = (3.14 * (r**2))
        return area
    except TypeError as te:
        return "Ouch..that's an error!", te


print(find_area("3"))
print(find_area(-3))
