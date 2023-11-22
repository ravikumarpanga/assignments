#wrt a program to revers an intiger in python 
"""num=input("Enter a number:")
rev=(str(num)[::-1])
print(rev)"""

# Write a program in Python to check whether an integer is Armstrong number or not.

# Take two numbers check which one is greater among them

"""r=int(input("Enter a number of r:"))
s=int(input("Enter a number of s:"))
if r>s:
    print("r is greater then s")
else:
    print("s is greater then r")"""


# r=int(input("Enter a number of r:"))
# s=int(input("Enter a number of s:"))
# if r>s:
#     print("r is greater then s")
# elif r<s:
#     print("s is greater then r")

day=int(input("enter a date:"))
month=int(input("enter a month:"))
year=int(input("enter a year:"))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    max_days=31
elif  month==4 or month==6 or month==9 or month==11:
    max_days=30
elif month==2 and (year%4==0 and year%100!=0) or year%400==0:
    max_days=29
else:
    max_days=28
if day<1 or day>max_days:
    print("date is in valid check the date again")
elif month<1 or month>12:
    print("month is in valid check the month again")
else:
    print("valid date")
