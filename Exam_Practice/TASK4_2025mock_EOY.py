count = 0 # 6 count should start from 0
total = 0
max_score = 0 # 4 max_score should start from 0
min_score = 50

print("Enter student scores (0-50). Enter -1 to send.")
score = int(input("Enter score: ")) # 1 add bracket
while score != -1:
    if score > 0 and score < 50:# 5 change or to and
        count += 1
        total = total + score
        if score > max_score:
            max_score = score
        elif score < min_score:
            min_score = score
else:
    print("Invalid score! Please enter 0 - 50 only") # 2 extra indentation
    score = int(input("Enter score: "))

print("Processing results...")
if count == 0: # 3 more equal sign
    print("No scores were entered")
else:
    average = total / count # 7 should only be 1 slash
    print(f"Number of scores: {count}")
    print(f"Maximum score: {max_score}\tMinimum score: {min_score}")
    print(f"Average score: {average}") #8 should be an f string