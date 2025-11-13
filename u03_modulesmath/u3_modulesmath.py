# <str>.format()

name = "John"
hobby = "Swimming"
print("{} likes {}".format(name, hobby))

print(f"{name} likes {hobby}")



colors = "red,blue,green,orange,red,blue,green,orange,red,blue,green,orange,red,blue,green,orange,red,blue,green,orange,red,blue,green,orange,red,blue,green,orange,red,blue,green,orange,red,blue,green,orange,red,blue,green,orange,red,blue,green,orange"

color_list = []
tempword = ""

for char in colors:
    if char == ",":
        color_list.append(tempword)
        tempword = ""
    else:
        tempword = tempword + char
        print(tempword)

print(color_list)
