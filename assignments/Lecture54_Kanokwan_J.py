def login():
    usernameInput = input("Username: ")
    passwordInput = input("Password: ")
    if usernameInput == "owner" and passwordInput == "1234":
        showMenu()
    else:
        print("Incorrect username or password.")

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator (Net sum)")
    selectMenu()

def selectMenu():
    userSelected = int(input(">> "))
    if userSelected == 1:
        totalPrice = int(input("Enter total price (THB): "))
        result = vatCalculator(totalPrice)
        print("Total price with VAT:", result, "THB")
    elif userSelected == 2:
        result = priceCalculator()
        print("Total price (net):", result, "THB")  # Net value, no VAT added
    else:
        print("Invalid selection.")

def vatCalculator(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result

def priceCalculator():
    price1 = int(input("First Product Price: "))
    price2 = int(input("Second Product Price: "))
    total = price1 + price2
    return total
login()
