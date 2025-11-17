# from random import randint
# firstname = input("Enter first name: ")
# lastname = input("Enter last name: ")
# library_id = firstname + lastname
# print("Library ID is " + library_id)
# pin = ""
# for i in range(4):
#     pin += str(randint(0,9))
# print("PIN is " + pin)

#Task 2.1(a)
# from random import randint
# firstname = input("Enter first name: ")
# lastname = input("Enter last name: ")
# year = "2025"
# library_id = firstname[0] + lastname[-3:] + year
# print("Library ID is " + library_id.upper())
# pin = ""
# for i in range(4):
#     pin += str(randint(0,9))
# print("PIN is " + pin)

# Task 2.1 (b)

# from random import randint
# firstname = input("Enter first name: ")
# lastname = input("Enter last name: ")
# year = "2025"
# library_id = firstname[0] + lastname[-3:] + year
# print("Library ID is " + library_id.upper())
# pin = ""
# for i in range(6):
#     pin += str(randint(0,9))
# print("PIN is " + pin)

# Task 2.2 
from random import randint
firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
year = "2025"
library_id = firstname[0] + lastname[-3:] + year
print("Library ID is " + library_id.upper())
pin = ""

attempts = 0 
while attempts < 3:
    pin = ""
    for i in range(6):
        pin += str(randint(0,9))
    print("PIN is " + pin)
    
    ENTER_PIN = input("Please enter the pin: ")

    if ENTER_PIN == pin:
        print("Library account activated. ")
        verified = True
        break
    else:
        attempts += 1
        if attempts < 3:
            print("PIN not verified! New PIN generated.")
        else:
            print("Inactive account! ")



