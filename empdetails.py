def empdetails():
    s={}
    name=input("enter a empname:")
    domain=input("enter a domain:")
    empid=input("enter a empid:")
    email=input("enter a email:")
    s["name"]=name
    s["domain"]=domain
    s["empid"]=empid
    s["mail"]=email
    print(s)
empdetails()
