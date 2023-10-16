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




