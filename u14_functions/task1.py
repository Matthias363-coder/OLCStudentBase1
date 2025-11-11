###################################################
# Part 1: Learning Exercises

# Exercise 1: A Simple Function
# # Define a function that prints "Hello, World!" and call it.
# # Call the function
# def hello():
#     print("Hello, World!")

# hello()





#------------------------------------------------------------
# Exercise 2: Function with One Parameter
# Define a function that takes a name as a parameter and greets the user.
# Call the function with your name.
# def greet(yourname):
#     print(f"Hello {yourname}")


# greet("matthias")

# def intro(yourname, myname):
#     print(f"Hello {yourname}, I am {myname}")

# intro("Matthias", "Savvy")





#------------------------------------------------------------
# # Exercise 3: Function with Two Parameters
# # Define a function that takes two numbers and prints their sum.
# # Call the function with two numbers.


# def add(num1, num2):
#     answer = num1 + num2

#     print(f"{num1} + {num2} = {answer}")

# add(34,98)






#------------------------------------------------------------
# Exercise 4: Function with a Return Value
# Define a function that calculates the area of a rectangle.
# # Call the function and store the result.
def area_rectangle(length, breadth):
    area = length * breadth

    return area

area1 = area_rectangle(34,76)
area2 = area_rectangle(12,32)
area3 = area_rectangle(54,54)
area4 = area_rectangle(87,465)
area5 = area_rectangle(24,85)

total = area1 + area2 + area3 + area4 + area5

print(total)

# line execution
#line 62, 57,58,60,63,57,58,59,63,64,57,58,59


#------------------------------------------------------------
# Exercise 5: Using Returned Values in Further Computations
# # Define a function that calculates the perimeter of a rectangle.
# def calculate_perimeter(length, width):
#     return 2 * (length + width)

# # Use both functions to calculate the area and perimeter.
# length = 6
# width = 4
# area = calculate_area(length, width)
# perimeter = calculate_perimeter(length, width)
# print("For a rectangle of length {} and width {}:".format(length, width))
# print("Area: {}, Perimeter: {}".format(area, perimeter))





#------------------------------------------------------------
# Exercise 6: Demonstrating Local and Global Variables
# Define a function that modifies a local variable.
# def local_variable_example():
#     x = 10  # Local variable
#     print("Inside the function, x is {}".format(x))

# # Outside the function.
# x = 20  # Global variable
# local_variable_example()
# print("Outside the function, x is {}".format(x))




