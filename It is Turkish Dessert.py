def forwardSlash(count):
    for i in range(int(count)):
        print("/",end="")


def backSlash(count):
    for i in range(int(count)):
        print("\\",end="")

def space(count):
    for i in range(int(count)):
        print(" ",end="")

def nextLine(count):
    for i in range(int(count)):
        print()

def topSide(radius):
    firstLine = radius / 2 - 1 
    for i in range(int(radius/2)):
        space(firstLine-i)
        forwardSlash(1)
        space(i*2)
        backSlash(1)
        nextLine(1) 

def bottomSide(radius):
    firstLine = radius - 2
    for i in range(int(radius/2)):
        space(i)
        backSlash(1)
        space(firstLine - i * 2)
        forwardSlash(1)
        nextLine(1)

def paintIt(count):
    topSide(count)
    bottomSide(count)

count = int(input("Give me a number for radius of Baklava : "))
if count % 2 != 0:
    count +=1
elif count == 2:
    print("\nThis is so small piece :(")
elif count < 2:
    count = 4

paintIt(count)
print("Also, Baklava is an extremely delicious Turkish dessert!\n")
