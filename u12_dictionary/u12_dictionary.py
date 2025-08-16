menu = {"hamburger": 6,
        "pizza": 15,
        "fries": 5,
        "coke": 2}

# # how to retrieve a value from the dictionary
# # example retrieve price of pizza
# pizzaprice = menu["pizza"]
# print(f"The price of pizza is ${pizzaprice}")

# how to add a new key value/ pair into dictionary
# print(menu) # before adding
# menu["hotdog"] = 9
# print(menu) # after adding

# how to change the value of key/ value pair
# menu["hamburger"] = 10
# print(menu)

# check for existence for a key in dictionary
# choice = input("What do you want to eat?: ")
# price = menu[choice]
# if choice in menu:
#     print(f"Yes, I sell {choice} and it is ${price}: ")
# else:
#     print(f"Sorry, I do not sell {choice}. Go next door.")

# how to loop through the items in the dictionary
# print("Welcome to my restaurant!")
# print("Here is the menu")
# for food,price in menu.items():
#     print(f"{food} : ${price}")


# the more traditional way of looping through dictionary
for food in menu:
    print(food) # loops through the key in dictionary
    print(menu[food]) # pulls out the value in dictionary