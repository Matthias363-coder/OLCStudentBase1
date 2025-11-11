# group_1 = []
# group_2 = []
# group_3 = []
# flag = True
# while flag:
#     first_name = input("Please enter the child's name: ").upper()
#     first_name = first_name[1]
#     age = input("Please enter the child's age: ")
#     if first_letter >= "A" and first_letter <= "M" and age > 10:
#         group_1 = group_1 + [first_name]
#     elif first_letter >= "M" or age > 10:
#         group_2 = group_2 + [first_name]
#     elif age < 10:
#         group_3 = group_3 + [first_name]
#         count += 1
#     more = input("Do you have another child to enter, Y or N?: ")
#     if more == "Y":
#         flag = False

# print("You have entered the names of", flag, "children")
# print("The members of group 1 are", group_1)
# print("The members of group 2 are", group_2)
# print("The members of group 3 are", group_3)


group_1 = []
group_2 = []
group_3 = []
count = 0 #2 add count
flag = True
while flag:
    first_name = input("Please enter the child's name: ").upper()
    first_letter = first_name[0] #1. Change first_name to first_letter, 4 change 1 to 0
    age = int(input("Please enter the child's age: ")) #3 Add int
    if first_letter >= "A" and first_letter <= "M" and age > 10:
        group_1 = group_1 + [first_name]
    elif first_letter > "M" and age > 10: #6 remove =, 9 change or to and
        group_2 = group_2 + [first_name]
    elif age <= 10: # 5. add =
        group_3 = group_3 + [first_name]
    count += 1  #10 count should happen to every loop
    more = input("Do you have another child to enter, Y or N?: ")
    if more == "N": #8 change Y to N
        flag = False

print("You have entered the names of", count, "children") #7 change flag to count
print("The members of group 1 are", group_1)
print("The members of group 2 are", group_2)
print("The members of group 3 are", group_3)






    