#reverse a string
"""s=input("enter a string:")
rev=''
i=0
while i<len(s):
    rev=s[i]+rev
    i+=1
print(rev)"""

#len()
"""s="Peacock is beautiful"
r=len(s)
i=0
while i<r:
    print(s[i],end="")
    i+=1"""


#find the lenght of the string
"""s=input("enter a string:")
print(len(s))
"""
# strip()

"""s=" Python is not easy to learn "
print(len(s))
g=s.strip()
print(len(g))"""

# lstrip()

"""s=" Python is not easy to learn"
print(len(s))
g=s.lstrip()
print(len(g))"""

# rstrip()

"""s="Python is not easy to learn "
print(len(s))
g=s.rstrip()
print(len(g))
"""

#comparing 2 string

"""s=input("enter a string1:")
r=input("enter a string2:")
if s==r:
    print("both strings are equal")
else:
    print("both strings are not equal")"""

"""s=input("enter a string1:")
r=input("enter a string2:")
if s<r:
    print("r is greaterthan s")
elif s>r:
    print("s is greaterthan r")
else:
    print("both are equal")"""


#find the index value

# find()
"""a=input("enter a string:")
print(a.find(" "))"""


"""a="hello world"
print(a.find("o",3,9))
print(a.rfind("o",3,9))"""

# index()
"""s=input("enter a main string:")
r=input("enter a sub string:")
if s.index(r):
    print(r,"is found")
else:
    print(r,"is not found")"""

"""r="hello india"
print(r[-1])"""

#count()

"""r="india is my country"
#print(r.count("i"))
print(r.count("i",0,4))"""

#a="""hello
#world"""
#g=" hi"
#print(a+g)

