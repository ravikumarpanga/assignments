#write a program to merge two lists
"""s=[1,2,3,4,5,6]
r=[7,8,9,10,"hello"]
a=s.extend(r)
print(s)"""
"""b=int(input("enter length: "))
a=[]
for i in range(b):
    char=int(input("value of index "+str(i)+": "))
    a.append(char)
s=int(input("enter length: "))
r=[]
for i in range(s):
    char=int(input("value of index "+str(i)+": "))
    r.append(char)
a.extend(r)
print(a)
"""

#how to find sum of list
"""a=[1,5,7,9,8]
b=sum(a)
print(b)"""

"""s=eval(input("enter a list:"))
r=[]
a=0
for i in s:
    r.append(i)
    a=a+i
print(a)"""

#print even numbers from list
"""c=eval(input("enter a input:"))
for i in c:
    if i%2==0:
        print(i)"""

#print odd numbers from list
"""c=eval(input("enter a input:"))
for i in c:
    if i%2==1:
        print(i)"""

#delete element of given index
"""s=[1,5,"hello",10,9,23]
if s.pop(3):
    print(s)"""

"""r=int(input("enter length: "))
v=int(input("character to be deleted : "))
s=[]
for i in range(r):
    char=int(input("value of index "+str(i)+": "))
    s.append(char)
for i in s:
    if i==char:
        s.remove(v)
print(s)"""


#delete element
"""a=[1,5,"hello",10,9,23]
b=a.remove(5)
print(a)"""

"""s=int(input("enter length: "))
r=int(input("character to be removed : "))
d=[]
for i in range(s):
    char=int(input("value of index "+str(i)+": "))
    d.append(char)
for i in d:
    if i==char:
        d.remove(r)
print(d)"""


#insert a element at a given location
"""s=[10,20,40,50,60]
r=s.insert(2,30)
print(s)"""

"""s=eval(input("enter a list: "))
d=[]
for i in s:
    d.append(i)
d.insert(2,10)
print(d)"""


#insert a element at end
"""s=[10,20,40,50,60]
r=s.append(30)
print(s)"""

"""m=eval(input("enter a list: "))
s=input("character to be inserted : ")
r=[]
for i in m:
    r.append(i)
r.append(s)
print(r)"""

#check the size of two list are same or not
"""s=input("enter a list of s:")
a=len(s)
r=input("enter a list of r:")
b=len(r)
if a==b:
    print("Both lists size is same")
else:
    print("Both lists size is not same")"""

