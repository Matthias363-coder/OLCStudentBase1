
###################################################
# Part 1: Learning Exercises

# Exercise 1: Variables and Assignments
# Assign values to variables and calculate their sum.
# Example: Assign 10 to a and 20 to b. Calculate their sum.
# a = 10
# b = 20
# sum_value = a + b

# print("Sum of a and b is:", sum_value)




#------------------------------------------------------------
# Exercise 2: Adding Comments
# Add a single-line and a multi-line comment in this code.
# Example: Add comments to explain what the code does.
# Single-line comment
"""
This is a multi-line comment.
It explains the code in detail.
"""
# print("Comments explain your code.")

# allows you to type anything u want
# allows you to easily hide code



#------------------------------------------------------------
# Exercise 3: String Concatenation
# Combine two strings to make a greeting.
# Example: Assign "Hello" to greeting and "John" to name.
# Combine them to display: "Hello John".
# greeting = "Hello"
# name = "John"
# message = greeting + " " + name
# print(message)

# concatenating strings with variable values
# Hello, [yourname]. My name is [myname]. I am [age] years old

yourname = "Matthias"
myname = "David"
age = "17" # integer


# type conversion int() str()

# option 1: use the plus to join
sentence1 = "Hello, " + yourname + ". My name is " + myname + ". I am " + str(age) + " years old."
print(sentence1)

# option 2: using the print() and commas
# does not work outside of print()
print("Hello, " , yourname , ". My name is " , myname , ". I am " , age , " years old.")

# option 3: use the .format()
sentence3 = "Hello, {}. My name is {}. I am {} years old.".format(yourname, myname, age)
print(sentence3)

# option 4: f strings
sentence4 = f"Hello, {yourname}. My name is {myname}. I am {age} years old."
print(sentence4)

#------------------------------------------------------------
# Exercise 4: String Repetition
# Repeat a phrase multiple times to create a pattern.
# Example: Print the phrase "Python is fun! " three times.
# phrase = "Python is fun! "
# print(phrase * 3)




#------------------------------------------------------------
# Exercise 5: Combining Variables
# Use variables to create a descriptive sentence.
# Example: Assign "Python" to language and "awesome" to
# adjective. Combine them to display: "Learning Python is
# awesome!"
# language = "Python"
# adjective = "awesome"
# print("Learning " + language + " is " + adjective + "!")



