# Scenario: Validate a password to ensure it is at least 8 characters long and contains:
# - At least one uppercase letter.
# - At least one lowercase letter.
# - At least one digit.

# Example:
# Input: "Secure123"
# Output: "Valid password"

# Input: "password"
# Output: "Invalid password"

## Bonus: Print out which of the requirement failed.
 

# while True: 
#     password = input("Enter your password: ")
#     has_upper = False
#     has_lower = False
#     has_digit = False
#     for char in password:
#         if char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         elif char.isdigit():
#             has_digit = True
    
#     if len(password) > 8 and has_upper and has_lower and has_digit:
#         print("Valid")
#         break
#     else:
#         print("Invalid password")
#     if len(password) < 8:
#         print("Password must be 8 characters long")
#     if not has_upper:
#         print("Password must have at least one uppercase letter")
#     if not has_lower:
#         print("Password must have at least one lowercase letter")
#     if not has_digit:
#         print("Password must have at least one digit")


    # looping through every character in password

        # as you loop through you check if this character has upper case

        # check if this char has lower case

        # check if this char has number
    


##############################################################################
# Assignment 16: Sentence Validation
# Scenario: Ensure a sentence starts with a capital letter and ends with a period.

# Example:
# Input: "The quick brown fox jumps over the lazy dog."
# Output: "Valid sentence"

# Input: "the quick brown fox jumps over the lazy dog"
# Output: "Invalid sentence: does not start with a capital letter and does not end with a period"

# Input: "Hello world"
# Output: "Invalid sentence: does not end with a period"

# how to retrieve first char and last char ? 
# word = "SINGAPORE"
# word[0] # retrieve first char
# word[-1] == "." # retrieve last char
while True:
    sentence = input("Enter a sentence that starts with a capital letter and ends with a period: ") 
    # sentence[-1] = "."
    if sentence[0].isupper() and sentence[-1] == ".":
        print("Valid")
        break
    else:
        print("Invalid")

####################################################
# Exercise 7: Extracting Middle Elements from a List
# Scenario: Extract the middle 3 elements from a list with an odd 
# number of elements.
numbers = [10, 20, 30, 40, 50, 60, 70]
middle = len(numbers) // 2
print("")