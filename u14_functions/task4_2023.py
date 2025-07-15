# takes in a string, and return the words in that string as a list
# def split_sentence(word_string): 
#     list_sentence = word_string.split() 
#     return list_sentence 

# def check_list(sentence, word):
#     words = split_sentence(sentence)
#     if word in words:
#         return "Yes"
#     else:
#         return "No"

# inputsentence = "today i want to eat hamburger"       
# wordtocheck = "eat"
# result = check_list(inputsentence, wordtocheck)
# print(result)
# sentence = "i want to eat macdonalds"

# sentencelist = split_sentence(sentence)
# print(sentencelist)
# Save the program as CHECK_LIST_2023_<your name>_<centre number>_<index number>.py [7 marks] 
# Extend the program by writing another function check_list() that searches 
# through the list of words to find a certain word. If it finds the word in the list, 
# it returns "Yes", otherwise it returns "No".  
# The variable word needs to be passed to the function.  
# The function you write must use the function split_sentence() already provided. 
# Save your program. 


# in keyword for existence check
# friends = ["john","mary","edward"]
# name = input("Enter a friend's name: ")

# if name in friends:
#     print(f"{name} is your friend. ")
# else:
#     print(f"{name} is not your friend. ")

def split_sentence(word_string): 
    list_sentence = word_string.split() 
    return list_sentence 

def check_list(sentence, word):
    words = split_sentence(sentence)
    if word in words:
        return "Yes"
    else:
        return "No"

inputsentence = "today i want to eat hamburger"       
wordtocheck = "eat"
result = check_list(inputsentence, wordtocheck)
print(result)

def reverse_sentence(sentence):
    listsentence = split_sentence(sentence)


    reversed = []
    for word in listsentence:
        reversed.insert(0, word)
    
    output = ""
    for word2 in reversed:
        output = output + word2 + " "

    print(reversed) # checking
    print(output)
    return output
    

# reverse_sentence[::-1]:

    



    #string slicing

reverse_sentence("the cat sat on the mat")
##################################################
### Task 2
# Extend your program by writing another function reverse_sentence() 
# that reverses the words in the string and returns the whole string
# reversed, with spaces between the words.  
 
# For example,  
# "the cat sat on the mat" would return: "mat the on sat cat the".  
 
# The function you write must use the function split_sentence() already provided.  
# You must not use the slice operator or the reverse function available in Python.  
# Your program does not need to consider any spaces before or after the reversed sentence. 
 
# Save your program.