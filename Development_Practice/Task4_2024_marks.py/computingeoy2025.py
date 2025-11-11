# character_power = {
#     'mario':50,
#     'luigi':45,
#     'bowser':80,
#     'peach':40,
#     'yoshi':55,
#     'toad':30,
#     'wario':70,
#     'daisy':42,
#     'waluigi':65,
#     'donkey kong':75,
# }

# character = input("Please enter the character name: ").lower()
# if character in character_power:
#     power = character_power[character]
#     print(f"The power of {character} is {power}")
# else:
#     print(f"{character} is not found in the data base")
# add = input("Would you like to add any of the entries (Y or N): ")


# Task 3.2

# character_power = {
#     'mario':50,
#     'luigi':45,
#     'bowser':80,
#     'peach':40,
#     'yoshi':55,
#     'toad':30,
#     'wario':70,
#     'daisy':42,
#     'waluigi':65,
#     'donkey kong':75,
# }


# character = input("Please enter the character name: ").lower()
# if character in character_power:
#     power = character_power[character]
#     print(f"The power of {character} is {power}")
# else:
#     print(f"{character} is not found in the data base")
    
# add = input("Would you like to add any of the entries (Y or N): ")


# # check if add is equal to Y
# if add == "Y":
    
#     # ask for an input for new character, to lower case
    
#     # check if exist, if exist then reprompt >>>> while Loop
#     while True:
#         new = input("Enter a character name: ")
#         if new in character_power:
#             print("Please enter another character")
#         else:
#             break
#     # ask for a number between 1 to 100

#     # keep asking until valid number from 1 to 100
#     while True:
#         power_num = int(input("Enter a number from 1 to 100: "))
#         if power_num >= 1 and power_num <= 100: #
#             break
#         else:
#             print("Please enter another number")
#     # add to dictionary
#     character_power[new] = power_num
#     # output dictionary
#     print(character_power)


character_power = {
    'mario':50,
    'luigi':45,
    'bowser':80,
    'peach':40,
    'yoshi':55,
    'toad':30,
    'wario':70,
    'daisy':42,
    'waluigi':95,
    'donkey kong':75,
}


character = input("Please enter the character name: ").lower()
if character in character_power:
    power = character_power[character]
    print(f"The power of {character} is {power}")
else:
    print(f"{character} is not found in the data base")
    
add = input("Would you like to add any of the entries (Y or N): ")


# check if add is equal to Y
if add == "Y":
    
    # ask for an input for new character, to lower case
    
    # check if exist, if exist then reprompt >>>> while Loop
    while True:
        new = input("Enter a character name: ")
        if new in character_power:
            print("Please enter another character")
        else:
            break
    # ask for a number between 1 to 100

    # keep asking until valid number from 1 to 100
    while True:
        power_num = int(input("Enter a number from 1 to 100: "))
        if power_num >= 1 and power_num <= 100: #
            break
        else:
            print("Please enter another number")
    # add to dictionary
    character_power[new] = power_num
    # output dictionary
    print(character_power)

# Task 3.3 - at the end of program
maxpower = 0
maxcharacter = 0
totalpower = 0
for character, power in character_power.items():
    if power > maxpower:
        maxpower = power
        maxcharacter = character
    totalpower = totalpower + power
print(f"The character with the highest power is {maxcharacter} with {maxpower}")
averagepower = totalpower / len(character_power)
round1 = round(averagepower, 1)
print(f"The average power for all the characters rounded off to 1 decimal place is {averagepower}")
# // >> floor divide >>> divide and round down
