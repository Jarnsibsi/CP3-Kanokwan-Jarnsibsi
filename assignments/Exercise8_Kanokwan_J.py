usernameInput = input("Username: ")
passwordInput = input("Password: ")
if usernameInput == "owner" and passwordInput == "1234":
    print("----Welcome to J shop----")
    print("1.Apple  10 THB")
    print("2.Pen     5 THB")
    print("3.Water  15 THB")
    print("-------------------------")
    userSelected = int(input("Please select items (e.g., 1 2 3): "))
    if userSelected ==1:
        price = int(input("How many Apple you want to buy ? : "))
        result1 = price*10
        print("Total :",result1,"THB") 
     
    elif  userSelected ==2:
        price = int(input("How many Pen you want to buy ? : "))
        result2 = price*5
        print("Total :",result2,"THB") 
    elif  userSelected ==3:
        price = int(input("How many Water you want to buy ? : "))
        result3 = price*15
        print("Total :",result3,"THB")
        
    else:
        print("Invalid selection.")
else:
    print("Incorrect username or password.")           

    


