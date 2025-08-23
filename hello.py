
bags_rice = 15
upper_bound = 5.1
lower_bound = 4.9
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
    if bag_weight < lower_bound:
        print("The bag of rice is underweight")

#         7       Edit the program so that it:

# a.       Accepts the weights for only 10 bags of rice.
# [1]

bags_rice = 10
upper_bound = 5.1
lower_bound = 4.9
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
    if bag_weight < lower_bound:
        print("The bag of rice is underweight")

# b.       Prints out the message “The bag of rice is the correct weight” when a weight entered is between 4.9kg and 5.1 kg inclusive.
# [2]
bags_rice = 15
upper_bound = 5.1
lower_bound = 4.9
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
    elif bag_weight < lower_bound:
        print("The bag of rice is underweight")
    elif lower_bound <= bag_weight <= upper_bound:
        print("The bag of rice is the correct weight")
# c.       Prints out the number of bags of rice that were underweight, as well as the number that were overweight, after the weights of all the bags have been entered.
# [5]
bags_rice = 15
upper_bound = 5.1
upper_bound_num = 0
lower_bound = 4.9
lower_bound_num = 0
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
        upper_bound_num += 1
    if bag_weight < lower_bound:
        print("The bag of rice is underweight")
        lower_bound_num += 1
print(f"The number of overweight bags of rice is {upper_bound_num}")
print(f"The number of underweight bags of rice is {lower_bound_num}")

# Save your program.

#       Save your program as VARBAGS_<your name>_<center number>_<index number>.py

# Edit your program so that it works for any number of bags of rice.
bags_rice = int(input("Enter the number of bags of rice: "))
upper_bound = 5.1
upper_bound_num = 0
lower_bound = 4.9
lower_bound_num = 0
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))
    if bag_weight > upper_bound:
        print("The bag of rice is overweight")
        upper_bound_num += 1
    if bag_weight < lower_bound:
        print("The bag of rice is underweight")
        lower_bound_num += 1
print(f"The number of overweight bags of rice is {upper_bound_num}")
print(f"The number of underweight bags of rice is {lower_bound_num}")

# Save your program.

# [2]