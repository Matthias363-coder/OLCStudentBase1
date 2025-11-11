###################################################
# Part 1: Learning Exercises


# Practice Exercise 1: Creating a Dictionary
# Create a dictionary to store student names and their grades.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
print(f"Student Grades: {students}")




#------------------------------------------------------------
# Practice Exercise 2: Accessing Dictionary Values
# Access Bob's grade from the dictionary.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
 # Access using the key
grade = students["Bob"]
print(f"Bobs grade is {grade}")





#------------------------------------------------------------
# Practice Exercise 3: Adding New Key-Value Pairs
# Add a new student, Diana, with a grade of 92 to the dictionary.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
 # Add new key-value pair
students["Diana"] = 92
print(students)





#------------------------------------------------------------
# Practice Exercise 4: Updating Existing Values
# Update Charlie's grade to 80 in the dictionary.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# Update value
students["Charlie"] = 88
print(students)




#------------------------------------------------------------
# Practice Exercise 5: Deleting Key-Value Pairs
# Remove Alice's entry from the dictionary.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
del students["Alice"]  # Delete key-value pair
print("Updated Student Grades: {}".format(students))





#------------------------------------------------------------
# Practice Exercise 6: Checking for Existence of a Key
# Check if 'Diana' is in the student dictionary.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}
while True:
    if "Diana" in students:
        print("Yes. Diana is in the student dictionary.")
    else:
        print("No. Diana is not in the student dictionary.")

    



#------------------------------------------------------------
# Practice Exercise 7: Iterating Through a Dictionary
# Print all student names and their grades.
students = {"Alice": 85, "Bob": 90, "Charlie": 78}

for name, grade in students.items():  # Iterate through dictionary
    print("{}: {}".format(name, grade))




#------------------------------------------------------------
# task here is to find the student who score the highest
# loop through the dictionary
maxgrade = 0
maxstudent = "" # to store the student with highest score
total_scores = 0

for student, grade in students.items():
    if grade > maxgrade:
        maxgrade = grade
        maxstudent = student

    # not in if condition
    total_scores = total_scores + grade

average = total_scores/ len(students)
print(average)

print(f"{maxstudent} scored the highest {maxgrade}")

num = 3.100
rounded2dp = round(num, 3)
rounded2dp2 = f"{num :.2f}"

print(rounded2dp)
print(rounded2dp2)



listnums = [23,45,6765,345342,37,7,34,745]
# max in the list algorithm

# assume the first number is the biggest
maxnum = listnums[0]

# loop through every single number in the list consecutively
for num in listnums:
    if num > maxnum:
        maxnum = num
        # if the next number is bigger, then store that number

print(maxnum)




