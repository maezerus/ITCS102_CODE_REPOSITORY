import getpass

u =  "maezzy123"
p = "01234"

isLogin = False #trigger

while isLogin == False:

    user = input("Please input username --->")
    password = getpass.getpass("Enter your password --->")
    
    if user == u and password == p:
        print("LOGIN SUCCESSFULLY!")
        isLogin = True
    
    else: 
        print("PLASE TRY AGAIN")
        isLogin = False
   