num = int(input("Enter a number: "))

try:
    a = 2*num-2
    for b in range(0,num):
        for c in range(0,a):
            print(end=" ")
        a = a-1
        for c in range(0,b+1):
            print("*", end=" ")
        print("\n")
except:
    print("Invalid Entry")

num2 = int(input("Enter a number: "))
try:
    a = 2*num2 -2
    for b in range(num2,-1,-1):
        for c in range(a,0,-1):
            print(end=" ")
        a = a +1
        for c in range(0, b+1):
            print("*", end=" ")
        print("\n")
except:
    print("Invalid Entry")

num3 = int(input("Enter a number: "))
try:
    for i in range(0, num3):
           for j in range(0, i + 1):
                print("*", end=" ")
           print("\n")
    for i in range(num3, 0 , -1):
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\n")
except:
    print("Invalid Entry")

num4= int(input("Enter a number: "))

try:
    k = 2 * num4 - 2
    for i in range(0, num4-1):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\n")
    k = -1
    for i in range(num4-1,-1,-1):
        for j in range(k,-1,-1):
            print(end=" ")
        k = k + 2
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\n")
except:
    print("Invalid Entry")



num5 = int(input("Enter a number: "))
try:
    for i in range(0,num5):
        for j in range(0, i+1):
            print("*" , end=" ")
        print("\n")
except:
    print("Invalid Entry")
    

num6 = int(input("Enter a number: "))
try:
    k = 2 * num6 - 2
    for i in range(0, num5):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("* ", end="")
        print("\n")
except:
    print("Invalid Entry")

num7 = int(input("Enter a number: "))
try:
    for i in range(num7, -1, -1):
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\n")
except:
    print("Invalid Entry")
