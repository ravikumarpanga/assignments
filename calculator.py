#write a program to create a calculator using functions (sum,sub,mul,div)

# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     return x / y

# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# while True:
#     choice = input("Enter choice(1/2/3/4): ")
#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: ")) 
#         num2 = float(input("Enter second number: "))
#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))
#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))
#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))
#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#           break
#     else:
#         print("Invalid Input")




class Calculator:
    def _init_(self):
        print("***MY CALCULATOR***")
        self.operations()
    
    def operations(self):
        print(''' Select Which operations do you need
        1.Addition
        2.Subtarction
        3.Multipliaction
        4.Divison
Press 1 for Add , 2 for sub, 3 for Mul, 4 for Div''')
        
        n = int(input("\nEnter the value:"))
        self.numbers = list(map(int,input("\nEnter number of values:").split()))
        if(n == 1):
            self.add(self.numbers)
        elif(n == 2):
            self.sub(self.numbers)
        elif(n == 3):
            self.mul(self.numbers)
        elif(n == 4):
            self.div(self.numbers)    
        else:
            print("PLEASE CHOOSE OPTIONS")
            self.operations()   

    def add(self,numbers):
        print(f'Sum of numbers is {sum(numbers)}')
        

    def sub(self,numbers):
        result = self.numbers[0]
        for i in self.numbers[1:]:
           result -= i  
        print(f'Subtraction of numbers is {result}')
           

    def mul(self,numbers):
        result = 1
        for i in self.numbers[0:]:
            result *= i 
        print(f'Multipliaction of numbers is {result}') 
         

    def div(self,numbers):
        result = self.numbers[0]
        for i in self.numbers[1:]:
           result /= i  
        print(f'Division of numbers is {result}')
                 
              
c = Calculator()
print("Thanks for using my calculator")

