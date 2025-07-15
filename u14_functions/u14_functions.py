# def greeting(yourname, myname):
#     print(f"Hello {yourname}")
#     print(f"My name is {myname}")

# greeting("Darius","Matthias")
    
# def areatriangle(base,height):
#     area = 0.5 * base * height
#     print(f"The area of a triangle is {area}")

# a1 = areatriangle(34,87)
# a2 = areatriangle(23,443)
# a3 = areatriangle(12,34)
# a4 = areatriangle(66,45)
# a5 = areatriangle(98,21)

# total = a1 + a2 + a3 + a4 + a5
# print(f"Total area is {total}")

# def number(cube):
#     outcube = cube ** 3
#     return outcube

# a1 = number(3)
# a2 = number(6)
# a3 = number(8)
# a4 = number(45)

# total = a1 + a2 + a3 + a4
# print(f"The sum of all these cubes are {total}")

# find the cube of 3, 6, 8, 45

# find the sum of all these cubes


# Exercise 1: Random Username Generator
# Write a function that generates a username based on the user's
# first name, last name, a random animal from a list, and a random number.

# List of random animals: ["Tiger", "Lion", "Bear", "Wolf", "Eagle"]
# Random number: Generated between 10 and 99

# Example:
# Input: First Name: "John", Last Name: "Doe"
# Random animal: "Tiger", Random number: 42
# Output: "JohnDoeTiger42"
 
import random
def username(firstname, lastname):
    animals = ["Tiger", "Lion", "Bear", "Wolf", "Eagle"]
    rananimal = random.choice(animals)
    rannumber = random.randint(0,99)

    username = firstname + lastname + rananimal + str(rannumber)
    return username

firstname = input("What is your first name: ")
lastname = input("What is your last name: ")

USERNAME = username(firstname, lastname)
print(f"Hello {firstname}, your username is {USERNAME}")