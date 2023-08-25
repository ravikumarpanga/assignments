# 1.Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

"""d=eval(input("enter a dict:"))
s=d["r"]=4
print(d)
print(type(d))"""

"""d=eval(input("enter a dict:"))
s=d.update({"a":5})
print(d)"""


# 2.Write a Python script to check whether a given key already exists in a dictionary.

"""dic =eval(input("enter a dict dic:"))
key = eval(input("enter a dict key:"))
x = list(dic.keys())
if(x.count(key) == 1):
    print("Present")
else:
    print("Not Present")"""


# 3.Write a Python program to iterate over dictionaries using for loops

"""dt =eval(input("enter a dict dic:")) 
for key in dt.keys():
    print(key)"""

"""for value in dt.values():
    print(value)"""

"""for key in dt:
    print(key, dt[key])"""


# 4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# Sample Dictionary
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

#dt =eval(input("enter a dict dic:"))
"""r=dict()
for i in range(1,15+1):
    r[i]=i**2
print(r)"""
    

# 5.Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'marolix technology'
# Expected output: {'m': 1, 'a': 1, 'o': 3, 'l': 2, 'i': 1, 'x': 1, 't': 1, 'e': 1,'c': 1, 'h': 1, 'n': 1, 'g': 1,'y':1}

"""string =eval(input("enter a string:")) 
r ={}
for i in string:
     r[i]=r.get(i,0)+1
print(r)"""


# 6. Write a Python program to sum all the items in a dictionary.


"""s={}
for i in range(5): 
    k=input("enter keys: ")
    v=int(input("enter values: "))  
    s[k]=v
r=0
for i in s.values():
    r=r+i
print(r) """

# 7.Write a Python program to combine two dictionary by adding values for common keys.
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

"""d1=eval(input("enter a items of d1:"))
d2=eval(input("enter a items of d2:"))
d3 =dict(d1)
d3.update(d2)
for key,value in d1.items():
    for s,r in d2.items():
        if key == s:
            d3[key]=(value+r)
print(d3)"""


# 8.Write a Python program to access dictionary key's element by index.
# Expected Output:
# physics
# math
# chemistry

"""dt =eval(input("enter a dict :"))
print(list(dt)[0])
print(list(dt)[1])"""

# 9.Write a Python program to remove a key from a dictionary.

"""dt =eval(input("enter a dict :"))
key=input("Enter key to be removed: ")
del dt[key]
print(dt)"""

# 10.Write a Python script to merge two Python dictionaries.d
"""dt1=eval(input("enter a dict :"))
dt2=eval(input("enter a dict :"))
dt2.update(dt1)
print(dt1)"""