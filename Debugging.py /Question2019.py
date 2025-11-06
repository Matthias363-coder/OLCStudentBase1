# colour_list = ['red','green', 'blue','orange', 'purple','yellow']
# colour_to_find = input("Which colour would you like to search for? ")
# items = len(colour_to_find)
# item_number = 0
# colour_found = False
# while colour_found == True:
#     while item_number > items:
#         if colour_list[item_number] = colour_to_find
#             print("There are " + str(item) + " colours in the list, " + colour_to_find + " is item " + str(iten_number - 1) + " in the list.")
#             colour_found = True
#             item_number = item_number
#         elif item_number == items - 1:
#             print("The colour is not in the list. ")
#             colour_found = False
#             item_number = items
#         else:
#             item_number = items









colour_list = ['red','green', 'blue','orange', 'purple','yellow']
colour_to_find = input("Which colour would you like to search for? ")
items = len(colour_list) # 5. change colour_to_find to colour_list
item_number = 0
colour_found = False
while colour_found == False: # 6. change True to False
    while item_number < items: # 7. change greater than to lesser than
        if colour_list[item_number] == colour_to_find: # 1. Extra = 2. add colon
            print("There are " + str(items) + " colours in the list, " + colour_to_find + " is item " + str(item_number - 1) + " in the list.") # 3. add s to item 4. change iten_number to item_number
            colour_found = True
            item_number += 1 # 8. change = item_number to += 1
        elif item_number == items - 1:
            print("The colour is not in the list. ")
            colour_found = False 
            item_number = items
        else:
            item_number += 1