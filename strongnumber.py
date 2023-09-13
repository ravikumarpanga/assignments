#define a function to check weather the given number is strom number or not
# def strong(a):
#     out=0
#     for i in a:
#         t=1
#         for j in range(1,int(i),1):
#             t*=j
#         out+=t
#         if out==int(a):
#             print("strong num")
# strong(input("enter a number:"))

# def strong(n):
#     for a in range(1,n+1):
#         out=0
#         for i in str(a):
#             t=1
#             for j in range(1,int(i)+1):
#                 t*=j
#             out+=t
#             if out==a:
#                 print(a)
# strong(int(input("enter a number:")))

#leap year or not

# def leapyear(a):
#     if (a%4==0) and (a%100!=0) or (a%400==0) :
#         print("it is a leap year")
#     else:
#         print("it is not a leapyear")
# leapyear(int(input("enter a year:")))

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