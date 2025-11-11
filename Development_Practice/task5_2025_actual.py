# Task 5.1

# Write a function total_cost() that calculates the total cost of a sale by:
# taking cost as a parameter
# calculating the total cost by adding 9% for tax purposes
# returning the total cost
# Save your program.
# [3]
from asyncio import Task


def total_cost(cost):
    tax_rate = 0.09
    total = cost + (cost * tax_rate)
    return total

 

# Task 5.2

# Copy and paste your program from sub-task 5.1.

# A discount may be applied to a customer’s purchase.

# Extend the program by writing a function discount() that:

# takes cost as a parameter
# deducts a discount of 5% from the total cost if the total cost is between $50 (inclusive) and $100 (exclusive)
# deducts a discount of 10% from the total cost if the total cost is $100 or greater
# returns the total cost with or without a discount as appropriate
# Your function must use the function total_cost() to calculate the total cost for the sale.

# Save your program.
# [4]

def total_cost(cost):
    tax_rate = 0.09
    total = cost + (cost * tax_rate)
    return total


def discount(cost):
    
    total = total_cost(cost)

    if 50 <= total < 100:
        total -= total * 0.05  
    elif total >= 100:
        total -= total * 0.10  

    return total



# Task 5.3

# Copy and paste your program from sub-task 5.2.

# A customer receives reward points on a purchase.

# Extend your program by writing another function reward_points() that:

# takes the total cost with any discount applied as a parameter
# calculates the number of reward points received for the purchase. A customer receives 3 reward points for each whole dollar ($) spent
# returns the number of reward points received.
# Save your program.
# [3]


# Task 5.4

# Copy and paste your program from sub-task 5.3.

# A customer may receive a voucher code that can be used for a future purchase. ✓

# Extend your program by writing a function voucher() that:

# takes the total cost with any discount applied and the customer’s first name as parameters
# creates a voucher code that is the first three letters of the customer’s name then the string "05PERCENT", if the total cost is between $25 (exclusive) and $50 (inclusive)
# creates a voucher code that is the first three letters of the customer’s name then the string "10PERCENT", if the total cost is greater than $50
# returns the voucher code or None as appropriate.
# Save your program.
# [3]

