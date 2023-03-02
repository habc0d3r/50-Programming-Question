"""This is just a very simple program to generate required number of lines of code with different value"""
import random


def generate(x):
    for i in range(x):
        n = random.randint(0, 100)
        try:
            with open("result.txt", 'a') as file:
                file.write(f"print(is_prime({n}))\n")
        except IOError:
            print("File writing error...!")


generate(10)
