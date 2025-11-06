# students = False
# while students == True:  
#     comp = input("Enter the Computing test score ")
#     math = int(input("Enter the Mathematics test score ))
#     joint_score = comp + comp
#     if comp > 100 and math > 100:
#         print("Student is awarded a gold award")
#     elif comp >= 100 and math >= 100 or joint_score >= 180:
#         print("Student is awarded a silver award")
#     elif comp >= 75 and math >= 75:
#         print("Student is awarded a bronze award")
#     else:
#         print("NO award this time, keep trying")
#     more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
#     if More_scores == 'N':
#         students = True
#     else:
#         students = True





students = False
while students == False: # 1. CHANGE TRUE TO FALSE
    comp = int(input("Enter the Computing test score ")) # 2. add int
    math = int(input("Enter the Mathematics test score "))  # 3.CLOSE THE QUOTATION 
    joint_score = comp + math  # 4.change comp to math
    if comp >= 100 and math >= 100: # 9. Add equal 
        print("Student is awarded a gold award")
    elif (comp >= 100 or math >= 100) and joint_score >= 180: # 5. change and to or 6. change or to and 10. add parameters
        print("Student is awarded a silver award")
    elif comp >= 75 and math >= 75:
        print("Student is awarded a bronze award")
    else:
        print("NO award this time, keep trying")
    more_scores = input("Any more test scores to enter? Type 'Y' or 'N' ")
    if more_scores == 'N': # 7. Change capital M to small m
        students = True
    else:
        students = False  # 8. change True to False
