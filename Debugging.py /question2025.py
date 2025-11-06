# age = 0
# height = float(0) 
# rejected = 100
# rider = 0
# age = int(input("Please enter your age ))
# height = float(input("Please enter your height ")) 
# while age <> 0 and height != 0:
#     if age < 7 or age > 70 or height <= 1.3: 
#         if age < 7:
#             print("You are too young to ride") 
#         if age > 90:
#             print("You are too old to ride") 
#         if height <= 1.3:
#             print("You are too short to ride") 
#         rejected = rejected - 1
# else:
#         print("You can ride the Roller Coaster") 
#         rider = Rider + 1
#     age = int(input("Please enter your age "))
#     height = float(input("Please enter your height ")) 
# print("Number of people rejected ", rider) 
# print("Number of riders ", rejected)

age = 0
height = float(0) 
rejected = 0 # 1. Change from 100 to 0
rider = 0
age = int(input("Please enter your age" )) # 2. Close 
height = float(input("Please enter your height ")) 
while age != 0 and height != 0: # 3. Change to does not equal to 
    if age <= 7 or age > 70 or height <= 1.3: # 6. add =
        if age <= 7: # 4. add =
            print("You are too young to ride") 
        if age > 70: # 5. Change 90 to 70
            print("You are too old to ride") 
        if height <= 1.3:
            print("You are too short to ride") 
        rejected = rejected + 1 # 6. Change - to +
        age = int(input("Please enter your age ")) # 7. missing input
        height = float(input("Please enter your height ")) # 8. should be asked for each loop
    else: # 9. indentation error
        print("You can ride the Roller Coaster") 
        rider = rider + 1 # 10. Change Rider to rider
        age = int(input("Please enter your age "))
        height = float(input("Please enter your height ")) 
print("Number of people rejected ", rejected) 
print("Number of riders ", rider) # 11. rider and rejected are flipped
