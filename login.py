def login():
    d={
       "Ravi23":"123",
       "ram456":"2345",
       "sam145":"5567",
       "sitha":"6789"
       }
    username = input ("Username: ")
    password = input ("Password: ")
    for key in d.keys():
        if key==username:
            for value in d.values():
                if value==password:
                    print("your login  successfull")
                    break
            else:
                print("your userid and password is wrong try again")
        
            
login()