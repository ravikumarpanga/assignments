#write a python program to remove character from string

"""input_string=input("enter a string:")
charater_to_remove=input("enter the character to remove:")
s=input_string.replace(charater_to_remove,"")
print("modified string:",s)"""

#write a program to check string is palindrome or not

"""st=input("enter a string:")
r=st[::-1]
if st==r:
    print("yes, it's palindrome")
else:
    print("no, it's not a palindrome")"""

#write a python program to check given character is vowel or consonant

"""char=input("enter a character:")
for i in range(ord('a'),ord('z')+1):
    if char(i) not in ("aeiou"):
        print("it's consonant")
    else:
        print("vowel")"""

#write a python program to replace string space with given character in python

"""s=input("enter a string:")
r=s.replace(" ","_")
print(r)"""

#write a python program to count alphabets, digits, and special character in python

"""r=input("enter a string:")
alphabet=0
digit=0
specialcharacter=0
for i in r:
    if i.isalpha():
        alphabet+=1
    elif i.isdigit():
        digit+=1
    else:
        specialcharacter+=1
print("alphabet=",alphabet,"digit=",digit,"specialcharacter=",specialcharacter)"""

#write a python program to remove all the blank spaces in a given string

"""r=input("enter a string:")
s=r.replace(" ","")
print(s)"""

#write a python program to find some of integers in the string

"""r=input("enter a string:")
digit=0
for i in r:
    if i.isdigit():
        digit+=1
print("intigers=",digit)"""

#write a python program to remove repeated characters from string

"""s=input("enter a string:")
b=[]
i=0
while i<len(s):
    if s[i] not in b:
        b=b+ [s[i]]
    i+=1
print(b)"""

#write a python program to count occurrence of given character in string 

"""s="hello world"
count=0
for i in s:
    if i =="l":
        count+=1
print("count=",count)"""

"""s="hello world"
count=s.count('l')
print("count=",count)"""

#write a python program to check string is anagrams or not in python

str1 = input ("Enter string 1: ")
str2 = input ("Enter string 2: ")
str1 = str1.lower()
str2 = str2.lower()
if(len(str1) == len(str2)):
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    if(sorted_str1 == sorted_str2):
        print(str1 + " and " + str2 + " are anagram.")
    else:
        print(str1 + " and " + str2 + " are not anagram.")
else:
    print(str1 + " and " + str2 + " are not anagram.")

"""str1 = str(input ("Enter string 1: "))
str2 = str(input ("Enter string 2: "))
l1=[]
l2=[]
for i in str1:
  l1.append(i.lower())
l1.sort()
for j in str2:
  l2.append(j.lower())
l2.sort()
print("List 1 after sorting: ", l1)
print("List 2 after sorting: ",l2)
"""


#Write a Program to Sort the Characters of the String and First Alphabet Symbols followed by Numeric Values 
"""string=input("Enter a string: ")
alpha=[] 
digit=[] 
for c in string:
    if c.isalpha():
        alpha.append(c)  
    else:
        digit.append(c)
result=''.join(sorted(alpha)+sorted(digit))
print(result)"""