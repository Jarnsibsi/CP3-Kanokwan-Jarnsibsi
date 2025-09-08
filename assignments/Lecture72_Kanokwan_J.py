menuList = []

def showBill():
    print("---My Food---")
    priceTotal = 0
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        priceTotal += int(menuList[number][1])
    print("Total :", priceTotal)


while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])

showBill()
