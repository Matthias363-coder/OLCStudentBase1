
# Exercise 0: Modulus and Floor Division
# Write a program to calculate the modulus and floor division
# of two numbers. Example: 17 divided by 5.
# num1 = 17
# num2 = 5
# modulus = num1 % num2
# floor_div = num1 // num2
# print("17 % 5 is:", modulus)
# print("17 // 5 is:", floor_div)

#------------------------------------------------------------
# For Loops through List
#------------------------------------------------------------

# Exercise 1: Printing Items (Method 1)
# Given fruits = ["apple", "banana", "cherry"]
# Use a for loop to print each fruit directly.
# Output example:
# I like to eat apple.
# I like to eat banana.
# I like to eat cherry.

# fruits = ["apple", "banana", "cherry"]
# for i in fruits:
#     print(f"I like to eat {i}")





#------------------------------------------------------------
# Exercise 2: Printing Items (Method 2)
# Given the same fruits list
# Use for i in range(len(fruits)) to print the items.
# Output example:
# Fruit 1: apple
# Fruit 2: banana
# Fruit 3: cherry

# fruits = ["apple","banana","cherry"]
# for i in range(len(fruits)):
#     print(fruits[i])




#------------------------------------------------------------
# Exercise 3: Numbers Greater than 50
# Given numbers = [12, 67, 45, 89, 23]
# Use a for loop to print only numbers greater than 50.
# Expected Output:
# 67
# 89

# numbers = [12, 67, 45, 89, 23]
# for i in numbers:
#     if i > 50:
#         print(i)




#------------------------------------------------------------
# Exercise 4: Mapping Students to Scores
# students = ["Ali", "Bala", "Cindy"]
# marks = [55, 80, 62]
# Use a for loop to combine them into a dictionary.
# Expected Output:
# {"Ali": 55, "Bala": 80, "Cindy": 62}

# students = ["Ali", "Bala", "Cindy"]
# marks = [55, 80, 62]
# students_score = {}
# for i in range(len(students)):
#     current_student = students[i]
#     current_score = marks[i]

#     students_score[current_student] = current_score

# print(students_score)

# While Loop Validation
#------------------------------------------------------------

# Exercise 5: Length Check
# Keep asking user for a username until it has at least 5 characters.
# while True:
#     username = input("What is the username: ")
#     if len(username) >= 5:
#         break
#     else:
#         print("Invalid. username must be at least 5 characters long.")


# ----------------------------------------------------------------

# Exercise 6: Numbers Only
# Keep asking user to enter age until input contains digits only.

# while True:
#     age = input("Enter a age: ")
#     if age.isdigit():
#         break
#     else:
#         print("Invalid. age must be number")




# ----------------------------------------------------------------

# Exercise 7: Uppercase Only
# Keep asking until user enters a code in uppercase letters only.

# while True:
#     code = input("Enter a code in uppercase letters only: ")
#     if code.isupper():
#         break
#     else:
#         print("Invalid. code must be uppercase.")



# ----------------------------------------------------------------

# Exercise 8: Lowercase Only
# Keep asking until user enters an email in lowercase only.

# while True:
#     email = input("Enter a email in lowercase letters: ")
#     if email.islower():
#         break
#     else:
#         print("Invalid. email must be lowercase.")




# ----------------------------------------------------------------

# Exercise 9: Password Validation
# Keep asking until user enters a password with length >= 8.

while True:
    password = input("Enter a password with length >= 8: ")
    if len(password) >= 8:
        break
    else:
        print("Invalid. password must be length >= 8")




# (a) Input and validation [5 marks]
# Write a function get_valid_number(base) that:
# •	Accepts a parameter base which can be 2 or 10.
# •	Repeatedly asks the user to enter a number in that base until a valid number is provided.
# •	Checks that:
# o	For base 2: input only contains characters 0 and 1.
# o	For base 10: input only contains digits 0–9 (treat the value as a non-negative integer).
# •	Returns the number string (no leading/trailing spaces).
# Hint: Use .strip() and validate all characters before returning.

def get_valid_number(base):
    while True:
        number = input(f"Enter a number is base {base}: ")

        if base == "2":
            for i in number:
                if i not in "01":
                    isValid = False
        elif base == "10":
            for i in number:
                if int(i) <0 or int(i) >9:
                    isValid = False
        else:
            isValid = False
            print("Number must be either 2 or 10.")

        if isValid:
            return number
        else:
            print(f"{number} is not valid for base {base}")





# ----------------------------------------------------------------
# (b) Binary → Denary [6 marks]
# Write a function bin_to_den(binstring) that:
# •	Reverses the string so the least significant bit is processed first,
# •	Forms a place-value list [2**0, 2**1, …] matching the string length,
# •	Multiplies each bit by its positional weight and accumulates the total,
# •	Returns the denary integer.
# Example: bin_to_den("11111011") should return 251.




# ----------------------------------------------------------------