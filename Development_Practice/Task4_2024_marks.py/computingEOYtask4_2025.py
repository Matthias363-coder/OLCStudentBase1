# # DEBUGGING ORIGINAL
# count = 1
# total = 0
# max_score = 50
# min_score = 50

# print("Enter student scores (0-50). Enter -1 to send.")
# score = int(input("Enter score: ")
# while score != -1:
#     if score > 0 or score < 50:
#         count += 1
#         total = total + score
#         if score > max_score:
#             max_score = score
#         elif score < min_score:
#             min_score = score
# else:
#         print("Invalid score! Please enter 0 - 50 only")
#     score = int(input("Enter score: "))

# print("Processing results...")
# if count = 0:
#     print("No scores were entered")
# else:
#     average = total // count
#     print(f"Number of scores: {count}")
#     print(f"Maximum score: {max_score}\tMinimum score: {min_score}")
#     print("Average score: {average}")

# DEBUGGING ORIGINAL
count = 0 #6 count should start 0
total = 0
max_score = 0  # 5 Should start from 0
min_score = 50

print("Enter student scores (0-50). Enter -1 to send.")
score = int(input("Enter score: ")) #1 missing bracket
while score != -1: 
    if score > 0 and score < 50: # 9 should be and 
        count += 1
        total = total + score
        if score > max_score:
            max_score = score
        if score < min_score: #11 Cannot be elif
            min_score = score
    else: #8 Should be inside if condition
        print("Invalid score! Please enter 0 - 50 only") #2 indentation error
        
    score = int(input("Enter score: ")) #10 should be outside else condition

print("Processing results...")
if count == 0: #3 missing ==
    print("No scores were entered")
else:
    average = total / count #4 should not floor divide
    print(f"Number of scores: {count}")
    print(f"Maximum score: {max_score}\tMinimum score: {min_score}")
    print(f"Average score: {average}") #7 missing f string