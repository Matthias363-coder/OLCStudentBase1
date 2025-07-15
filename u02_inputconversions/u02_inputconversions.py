# input conversions

# use an input to store a name
# use an input to store an age

# print out f string
# My name is {} and I am {} years old.

# name = input("What is your name? ") # use input to ask for a name
# age = input("What is your age? ")
# print(f"My name is {name} and I am {age} years old")

# addition program
# ask for first number
# ask for second number
# add both of them up

# print out >>> 1 + 2 = 3
first_number = int(input("What is your first number? ")) # 5
second_number = int(input("What is your second number? ")) # 2
Total = first_number + second_number
print(f"{first_number} + {second_number} = {Total}")

var1 = "cat"
var2 = "dog"
var3 = var1 + var2 # a + on 2 strings >>> concatenation, "joins"
print(var3)

var4 = 1 # integer
var5 = 2
var6 = var4 + var5 # a + on 2 numbers will add
print(var6)

var7 = var1 + str(var4)
print(var7)

var8 = var1 * var5
print(var8)