# 1.Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

"""def uppercase_lowercase(string):
    upper=0
    lower=0
    for i in string:
        if (i>='A' and i<='Z'):
            upper=upper+1
        elif (i>='a' and i<='z'):
            lower=lower+1
        else:
            pass
    print("upper=",upper)
    print("lower=",lower)
s=input("enter a string:")
uppercase_lowercase(s)"""

# 2.Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]


"""def unique_list(n):
     unique = []
     for i in n :
         if i not in unique:
             unique.append(i)
     return unique
print(unique_list([1,2,3,3,3,3,4,5]))"""
    

# 3.Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog".

"""def is_pangram(s):
    c = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    phrase = ""
    for j in s:
        for i in alphabet:
            if j == i and j not in phrase:
                phrase += j
    for j in phrase:
        for i in alphabet:
            if j == i:
                c += 1
    if c == 26:
        print("Pangram")
    else:
        print ("not pangram")
myPhrase=input("enter a string:")
print (is_pangram(myPhrase))"""


#4.Write a Python function to create and print a list where the values are the squares of numbers between 1 and 10 (both included).


"""def printValues():
	l = list()
	for i in range(1,10+1):
		l.append(i**2)
	print(l)
		
printValues()"""

# 5.Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20 
"""def sum(num):
    total = 0
    for i in num:
        total=total+ i  
    print(total)
sum([8, 2, 3, 0, 7])"""



# 6.write a function to find sum of given values, pass values has variable number of arguments to function.

"""def sum(*args):
    total = 0
    for j in args:
        total=total+ j
    print(total)
s=sum(1,2,3,4,5)
print(s)"""