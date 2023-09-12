# def login():
#     d={
#        "Ravi23":"123",
#        "ram456":"2345",
#        "sam145":"5567",
#        "sitha":"6789"
#        }
#     username = input ("Username: ")
#     password = input ("Password: ")
#     for key in d.keys():
#         if key==username:
#             for value in d.values():
#                 if value==password:
#                     print("your login  successfull")
#                     break
#             else:
#                 print("your userid and password is wrong try again")
                    
# login()


def login(d):
    userid=input("enter a userid:")
    password=input("enter a  password:")
    s={}
    if userid in d:  
        if d[userid]==password:
            print("your login successful ")       
    else:
        print("userid and password is not valid")
        k=input("please enter new username: ")
        v=int(input("please enter new password: "))  
        s[k]=v
        print("new user is created:",s)
d={"Ravi23":"123",
          "ram456":"2345",
          "sam145":"5567",
          "sitha":"6789"
         }

login(d)