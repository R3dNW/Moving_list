#GitHub copy
class Item:
    name = ""
    description = ""


def clear():
    print("\n"*50)


counter = 0

###
items = {}

with open("Items.txt", "r") as f:
    item_file_text = f.read()

item_file_lines = item_file_text.split("\n")

for line in item_file_lines:
    line = line.split(",")
    if len(line) >= 2:
        item = Item()
        item.name = line[0]
        item.description = line[1]

        items[item.name] = item
###

list1 = list(items.values())
b = 1

print("Use 'w' and 's' to search and use 'x' to select.")

while b != "x":
    b = input()
    
    clear()
    if b == "w":
        counter = counter - 1
    elif b == "s":
        counter = counter + 1
    elif b == "x":
        break
        
    else:
        c = 0

    for i in range(0, len(list1)):
        print(list1[i].name)
        
        if i == counter:
            a = list1[i].description
            print(a)
        
        else:
            c = 0
        print()
        
print("You selected: " + list1[counter].name)
print("              " + list1[counter].description)
