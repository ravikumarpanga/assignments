#accessing string by index method
"""d="guido van rossum"
print(d[5])
print(d[-6])"""

#accessing string by using slicing method
"""a="Peacock is beautiful"
print(a[0:6-1:1])
print(a[11:19+1:2])
"""
#len()
"""s="Peacock is beautiful"
r=len(s)
i=0
while i<r:
    print(s[i],end="")
    i+=1"""

#reverse a string
"""s=input("enter a string:")
r=''
i=0
while i<len(s):
    r=s[i]+r
    i+=1
print(r)"""

#membership operators

m=[10,20,65,9,23,57,True,65,9,23,True]
b=[]
i=0
while i<len(m):
    if m[i]not in b:
        b=b+[m[i]]
    i+=1
print(b)