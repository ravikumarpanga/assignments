# print pattern with different shapes

"""c=int(input("enter a value:"))
for i in range(1,c+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()"""


c=int(input("enter a value:"))
for i in range(0,c):
    for j in range(0,c-i-1):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()