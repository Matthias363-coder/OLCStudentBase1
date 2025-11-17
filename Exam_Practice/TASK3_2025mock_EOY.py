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

# character = input("Please enter the character name: ")
# add = input("Would you like to add any of the entries (Y or N): ")


#Task 3.1
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
#     print(f"{character} has a power of {character_power[character]}")
# else:
#     print("character not found in database")
# add = input("Would you like to add any of the entries (Y or N): ")


#Task 3.2
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
#     print(f"{character} has a power of {character_power[character]}")
# else:
#     print("character not found in database")
# add = input("Would you like to add any of the entries (Y or N): ")
# while True:
#     if add == "Y":
#         new_character = input("Enter the new characters name: ").lower()
#         new_power = int(input("Enter the new character's power level: "))
#         if new_character in character_power:
#             print("Please try again.")
#         else:
#             character_power[new_character] = new_power
#             print("New character has been added to database")
#             print(character_power)
#             break

#Task 3.3
character_power = {
    'mario':50,
    'luigi':45,
    'bowser':80,
    'peach':40,
    'yoshi':55,
    'toad':30,
    'wario':70,
    'daisy':42,
    'waluigi':65,
    'donkey kong':75,
}

character = input("Please enter the character name: ").lower()
if character in character_power:
    print(f"{character} has a power of {character_power[character]}")
else:
    print("character not found in database")
add = input("Would you like to add any of the entries (Y or N): ")
while True:
    if add == "Y":
        new_character = input("Enter the new characters name: ").lower()
        new_power = int(input("Enter the new character's power level: "))
        if new_character in character_power:
            print("Please try again.")
        else:
            character_power[new_character] = new_power
            print("New character has been added to database")
            print(character_power)
            break

highest_power = 0
strongest_character = ""
for character in character_power:
    if character_power[character] > highest_power:
        highest_power = character_power[character]
        strongest_character = character
print(f"The character with the highest power is {strongest_character} with {highest_power}")

total_power = 0
count = 0

for power in character_power.values():
    total_power += power
    count += 1

average_power = total_power / count
round1dp = round(average_power, 1)
print(round1dp)






