#Sum of 1st n natural numbers using recursion
"""def natural(n):
    if n==0:
        return 0
    return natural(n-1)+n
n=natural(int(input("enter a value:")))
print(n)"""

#Define a recursive function to extract  all the string value present in given list only if the string value is having atleast "a" character
#sample=["raj","ramesh","suresh","ram","dancing"]
"""def sky(l,i=0,out=[]):
    if i>=len(l):
        return out
    if type(l[i])==str and ('a'in l[i] or 'a' in l[i]):
        out+=[l[i]]
    return sky(l,i+1,out)
s=sky(["raj","ramesh","suresh","ram","dancing"])
print(s)"""



#Wap to sort the list based on last character of the string.

"""def last_char(string):
    return string[-1]
last_char=lambda string:string[-1]
l=["raj","ramesh","suresh","ram","dancing"]
l.sort(key=last_char)
print(l)"""


#define a function which can take a string a return the last char in the string
"""
last=lambda string:string[-1]
print(last("hello"))"""

#wap to get all the vowels from the list
"""s=['a','b','c','d','e','f','g','h','i','j','k','o','u']
vowel=lambda char:char in "aeiouAEIOU"
res=filter(vowel,s)
print(list(res))"""

#wap to get even numbers from  the list 
"""even=lambda n: n%2==0
l=[10,20,30,40,50,60,2,5,6,10]
res=filter(even,l)
print(tuple(res))"""
