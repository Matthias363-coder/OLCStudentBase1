# num1 = 20
# num2 = 15

# if num1 > num2:
#     print(f"{num1} is bigger than {num2}")
#------------------------------------------------------------
# Exercise 11: Age-Based Group Assignment
# Write a program to categorize a person into groups based 
# on age: Child (0-12), Teen (13-19), Adult (20+).
# Example: Input = 15. Output = "Teen."

num = int(input("Enter a number"))
if num in range(0, 13):
    print("Child")
elif num in range(13, 20):
    print("Teen")
else:
    print("Adult")



#------------------------------------------------------------
# Exercise 12: Grade Checker
# Write a program to assign a grade based on marks:
# >= 90: A, >= 75: B, >= 60: C, < 60: D.
# Example: Input = 85. Output = "Grade B."

num = int(input("Enter a number: "))
if num >= 90:
    print("A")
elif num >= 75:
    print("B")
elif num >= 60:
    print("C")
else:
    print("D")

