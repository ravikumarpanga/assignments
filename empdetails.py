def add_emp():
    empdata = {}
    n=int(input("enter no.of emp:"))    
    for i in range(1,n+1):   
        domain = input("Enter the emp domain: ")
        name = input("Enter the emp name: ")
        empid = input("Enter the emp empid: ")
        email = input("Enter the emp email: ")
        empdetails = {"Domain": domain,"Name": name,"Email": email}
        empdata[empid] = empdetails
        print("Employee details added successfully!")
    print()
    domain = input("Enter which domain details do you want: ")
    found = False
    for key, value in empdata.items():
        if(value["Domain"] == domain):
            print(f"{key}: {value}")
            found = True
    if not found:
        print("No employees found with the specified domain.") 
add_emp()