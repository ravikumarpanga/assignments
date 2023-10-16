# class flipkart:
#     def __init__(self):
#         cart={}
#         Total_amount=0
#         number_of_items=0
#         while True:
#             self.Item=input("Enter a item name(q to quite):")
#             if self.Item == "q":
#                 break
#             else:    
#                 self.price=float(input("Enter a price:"))
#                 cart[self.Item]=self.price
#                 Total_amount+=self.price
#                 number_of_items+=1
                
#         print(cart)
#         print(f"Total amount={Total_amount}")
#         print(f"Total number of items={number_of_items}")
# s=flipkart() 

class ShoppingCart:
    def _init_(self):
        self.items_list = []
        self.prices = []
        self.menu()
    
    def menu(self):
        while True:
            print("Welcome to Shopping Cart Program!")
            print()
            print("Please select one of the following:")
            print("1. Add Items")
            print("2. View Cart")
            print("3. Remove Items")
            print("4. Compute Total")
            print("5. quit")           
            action = input("Please enter the action: ")
            print()          
            if(action == "1"):
                self.add_items()
            elif(action == "2"):
                self.view_cart()
            elif(action == "3"):
                self.remove_items()
            elif(action == "4"):
                self.compute_total()
            elif(action == "5"):
                self.quit()
            else:
                print("select any one of the following options")
            
    def add_items(self):
        Item = input("What item would you like to add: ")
        self.items_list.append(Item)
        price = float(input(f"what is the price of '{Item.capitalize()}': "))
        self.prices.append(price)
        
        print(f"'{Item.capitalize()}' has been added to the cart Successfully.\n")
        
    def view_cart(self):
        print("The Items in your Cart are: \n")
        for i in range(len(self.items_list)) and range(len(self.prices)):
            item = self.items_list[i]
            price = self.prices[i]
            items = (f'{i+1}. {item.capitalize()} - {float(self.prices[i])}')
            print(items)
            print()
    
    def remove_items(self):
        index = int(input("What item would you like to remove: "))
        self.items_list.pop(index-1)
        self.prices.pop(index-1)
        print("The selected item removed successfully")
        
    def compute_total(self):
        total = 0
        for i in range(len(self.items_list)):
            total += float(self.prices[i])
        print(f"The total price of the items in the shopping cart is {total}")
               
    def quit(self):
        print("Please visit us Again and spent some money here!")  
        print()
            
       
ShoppingCart()