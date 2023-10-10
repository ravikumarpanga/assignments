# class bank_atm:
#     def Atm_pin():
        
#             Creating_a_pin=int(input("Create a new pin:"))
#             if len(str(Creating_a_pin))==4:
#                     print("created pin successfully")
#                     while True:
#                         Enter_a_pin=int(input("Enter a pin:"))
#                         if Creating_a_pin==Enter_a_pin:
#                                print("your login successfully")
#                                break
#                         else:
#                                 print("your login pin is incorrect")                                
#             else:
#                     print("your pin must be 4digits")                  
#     Atm_pin()

#     def __init__(self,Balance):
#         self.Account_balance=Balance
#     def withdraw(self):
#         withdraw_amount=int(input("enter a amount:"))
#         self.Account_balance -=withdraw_amount
#     def checkbalance(self):
#             print(self.Account_balance)

# object=bank_atm(10000)
# print(object.Account_balance)
# object.withdraw()
# object.checkbalance()


class bank_atm:
    def Atm_pin():
        Creating_a_pin=int(input("Create a new pin must be 4digits:"))
        if len(str(Creating_a_pin))==4:
                print("created pin successfully")
                while True:
                        Enter_a_pin=int(input("Enter a 4digit pin:"))
                        if Creating_a_pin==Enter_a_pin:
                               print("your login successfully")
                               break
                        else:
                                print("your login pin is incorrect")                                
        else:
                print("your pin must be 4digits")                  
    Atm_pin()

    def __init__(self,Balance):
        print("Your Account balance =")
        self.Account_Balance=Balance
    def withdraw(self):
        while True:
            withdraw_amount=int(input("enter a withdraw amount:"))
            if self.Account_Balance>=withdraw_amount:
                self.Account_Balance-=withdraw_amount        
                print(f"Your withdraw_amount ={withdraw_amount} Rupees withdraw successfully")
                break
            else:
                  print("insufficient funds")
    def checkbalance(self):
            print(f"Your remaing Account_balance={self.Account_Balance} ")

object=bank_atm(10000)
print(object.Account_Balance)
object.withdraw()
object.checkbalance()



# user = {
#     'pin': int(input("enter a pin:")),
#     'balance':int(input("enter a balance:"))
# }

# def widthdraw_cash():
#     while True:
#         amount = int(input("Enter the amount of money you want to widthdraw: "))
#         if amount > user['balance']:
#             print("You don't have sufficient balance to make this widthdrawal")
#         else:
#             user['balance'] = user['balance'] - amount
#             print(f"{amount} Rupiess successfully widthdrawn your remaining balance is {user['balance']} Dollars")
#             print('')
#             return False

# def balance_enquiry():
#     print(f"Total balance {user['balance']} Rupiess")
#     print('')


# is_quit = False

# print('')
# print("Welcome to the ATM World")

# pin = int(input('Please enter your four digit pin: '))

# if pin == user['pin']:
#     while is_quit == False:
#         print("what do you want to do")
#         print(" Enter 1 to Widthdraw Cash \n Enter 2 for Balance Enquiry \n Enter 3 to Quit")

#         query = int(input("Enter the number corresponding to the activity you want to do: "))

#         if query == 1:
#             widthdraw_cash()
#         elif query == 2:
#             balance_enquiry()
#         elif query == 3:
#             is_quit = True

#         else:
#             print("Please enter a correct value shown")
# else:
#     print("Entered wrong pin")
