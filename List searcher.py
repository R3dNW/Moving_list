#GitHub copy
class Items:
    name = ""
    description = ""

def clear():
    print("\n"*50)


counter = 0

Health_potion = Items()
Health_potion.name = "--Health potion--"
Health_potion.description = "  It heals you by 3 health points."

Better_health_potion = Items()
Better_health_potion.name = "--Better health potion--"
Better_health_potion.description = "  It heals you by 5 health points."

Defence_potion = Items()
Defence_potion.name = "--Defence potion--"
Defence_potion.description = "  It raises your defence by 3 points."


list1 = [Health_potion,Better_health_potion,Defence_potion]
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

    for i in range(0,len(list1)):
        print(list1[i].name)
        
        if i == counter:
            a = list1[i].description
            print(a)
        
        else:
            c = 0
        print()
        
print("You selected: " + list1[counter].name)
print("              " + list1[counter].description)
