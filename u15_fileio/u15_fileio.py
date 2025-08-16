# with open('filename.txt','r') as fileobj:
#     # read the contents of the file
#     content = fileobj.read()

# print(content)


######## save data/write to a file
sentence = "\nI will do something else"

with open('newfile.txt', 'a') as fileobj:
    fileobj.write(sentence)

    # .readlines()
    # .writelines()