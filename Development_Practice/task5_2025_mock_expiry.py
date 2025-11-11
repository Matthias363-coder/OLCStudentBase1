#################################################################
#################################################################
# The task is to write a program that checks whether a food item has expired based on 
# its expiry date and today’s date. Dates are entered in the format "DD-MM".

# All code should have appropriate comments and meaningful identifiers.
# [2]
# ________________________________________
# Task 5.1
# Write a calculate_days( ) function that accepts a date parameter in the format "DD-MM".
# The function must calculate and return the total number of days elapsed since 01-01, assuming 30 days per month

# 4 marks
def calculate_days(date):
    day = date[:2]
    month = date[3:]

    day_num = int(day)
    month_num = int(month)

    days_in_month = 30

    total_days = (month_num - 1) * days_in_month + int(day)

    return total_days




print(calculate_days("01-02"))
print(calculate_days("30-01"))
print(calculate_days("30-02"))
print(calculate_days("30-12"))

# [4]
# ________________________________________
# Task 5.2
# Write a days_difference( ) function that takes two parameters:
# •	today (format "DD-MM")
# •	expiry (format "DD-MM")

# The function will check if an item has expired and return the number of days 
# between today’s date and the expiry date.
# •	Expiry is calculated by subtracting the today’s date from the expiry date. 
# You must use the calculate_days() function to retrieve the number of days between 
# today’s date and expiry date. Note that the number of days could be negative.
# You can assume both dates are always within the same year.
# [3]

# 3
def days_difference(today, expiry):
    today_date = calculate_days(today)
    expiry_date = calculate_days(expiry)

    differnence = expiry_date - today_date

    return differnence





# print(days_difference("01-01", "01-01"))
# print(days_difference("04-06", "14-06"))
# print(days_difference("14-06", "04-06"))

# ________________________________________
# Task 5.3
# Write a validate_date( ) function that accepts one parameter:
# •	date_str (a string in the format "DD-MM")
# The function must check whether the input date is valid according to the following rules:
# 1.	The input must contain a dash (-) separator between day and month.
# 2.	Both the day (DD) and month (MM) must be two characters long (e.g. "05-04" not "5-4").
# 3.	The day (DD) must be between 1 and 30 (inclusive).
# 4.	The month (MM) must be between 1 and 12 (inclusive).
# If all conditions are met, the function should return True.
# If any condition fails, the function should return False.
# Displays appropriate messages for invalid input. You may assume the input is always a string.
# [8]

# 8 
def validate_date(date_str):
    day = date_str[:2]
    month = date_str[3:]
    day_num = int(day)
    month_num = int(month)

    if len(date_str) != 5:
        print("Invalid. Must be 5 characters long. ")
        return False
    
    elif date_str[2] != "-":
        print("Invalid. Must have a dash inbetween the day and month.")
        return False
    elif day_num < 1 or day_num > 30:
        print("Invalid. Day must be between 1 and 30.")
        return False
    elif month_num < 1 or month_num > 12:
        print("Invalid. Month must be between 1 and 12. ")
        return False
    else:
        return True




trueorfalse = validate_date("01-001")
print(trueorfalse)


print(validate_date("01#01"))
# print(validate_date("aa-01"))
# print(validate_date("01-aa"))
print(validate_date("50-01"))
print(validate_date("05-50"))
print(validate_date("0310"))
print(validate_date("03-10"))

# ________________________________________
# Task 5.4
# Create a simple text-based user interface that:
# •	Prompts and validates today’s date in "DD-MM" format.
# o	You must use the validate_date() function to validate today’s date. 
# Your program will keep asking for an input until a valid date is provided.

# •	Prompts and validates the expiry date in "DD-MM" format.
# o	You must use the validate_date() function to validate the expiry date. 
# Your program will keep asking for an input until a valid date is provided.

# •	Compute if the item has expired. You must use the days_difference() function. 
#     If the number of days is positive, the item has not expired. 
#          Output “Item is fresh and will expire in <num> days.”
#     If the number of days is negative, the item has expired. 
#          Output “Item has expired <num> days ago.”
#     If the number of days is 0, then the item expires today. 
        #    Output “Item will expire today!”

# 2.5 + 15 = 17.5 + 2 = 19.5 / 25
# def user_interface():
while True:
    today_date = input("Enter a date in the format DD-MM: ")
    if validate_date(today_date):
        print("Valid.")   
        break
    else:
        print("Invalid! Please try again.")

while True:

    expiry_date = input("Enter a expiry date in the format DD-MM: ")
    if validate_date(expiry_date):
        print("Valid.")
        break
    else:
        print("Invalid! Please try again.")
    
days_expiry = days_difference(today_date, expiry_date)

if days_expiry > 0:
    print(f"Item is fresh and will expire in {days_expiry} days.")
elif days_expiry < 0:
    print(f"Item has expired {abs(days_expiry)} days ago.")
else:
    print("Item will expire today.")     
    
    # return days_difference

# print(user_interface)
# user_interface()
        
    



