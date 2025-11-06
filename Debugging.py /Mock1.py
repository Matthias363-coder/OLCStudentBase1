# A library program needs to keep track of books being 
# borrowed and returned. Each book has a unique ID 
# and a title. The program allows a user to input the 
# book ID and whether the book is being borrowed or returned.

# The program updates the status of the book accordingly 
# and displays a message. There are several syntax and 
# logic errors in the program.

### DO NOT CHANGE the first 3 lines of code.
books = {"1": "AVAILABLE", "2": "AVAILABLE", "3": "AVAILABLE", "4":"BORROWED"}
action = input("Enter 'B' to borrow a book or 'R' to return a book: ")
book_id = input("Enter the book ID: ")
### Make your code fixes after this

if action == "B":  # 1. need an extra =, 2. need a colon, 3. change to capital B
    if books[book_id] == "AVAILABLE": # 4. Change to all caps
        books["B"] = "borrowed"
        print("You have borrowed the book.")
    else:
        print("The book is already borrowed.")
elif action == "R": #5. Need an extra =, # 6. change to capital R
    if books[book_id] == "borrowed":
        books("R") = "returned" # 5. Change available to returned
        print("You have returned the book.") # 6. Forgot open inverted 
    else:# 7. indentation error
        print("The book is already returned.") # 8. Change available to returned
else: # 9. indentation error 
    print("Invalid action.") # 10. Forgot close inverted

print(books)