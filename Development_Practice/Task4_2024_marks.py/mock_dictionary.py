# student_scores = { 
#     'susan123':85, 
#     'randy329':92, 
#     'mike671':78, 
# } 
 
# def add_student(username, score): 
#     student_scores[username] = score 
#     print('Added {} with score {}'.format(username, score)) 
 

# def display_all(): 
#     for username in student_scores: 
#         print(username, student_scores[username]) 


student_scores = { 
    'susan123':85, 
    'randy329':92, 
    'mike671':78, 
} 
# Task 2.1

def add_student(username, score): 
    if username not in student_scores:
        print("Username does not exist.")
        student_scores[username] = score
        print('Added {} with score {}'.format(username, score)) 
    else:
        print("Username already exist.")
    


add_student('susan123', 85)
# add_student('peter123', 45)

print(student_scores)


# Task 2.2
def delete_student(username):
    if username not in student_scores:
        print("The username was not deleted.")
    else:
        del student_scores[username]
        print(f"Deleted {username}.")
    

# Task 2.3
def edit_score(username, newscore):
    if username in student_scores:
        student_scores[username] = newscore
        print(f"Updated {username}'s score to {newscore}")
    
    else:
        print("Username does not exist")
    
 

def display_all(): 
    for username in student_scores: 
        print(username, student_scores[username]) 
    

