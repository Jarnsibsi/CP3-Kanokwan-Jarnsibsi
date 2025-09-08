menuList = []
priceList = []


def showBill():
    print("---My Food---")
    priceTotal = 0
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        priceTotal += int(priceList[number])   
    print("Total :",priceTotal)
        

while True:
    menuName = input("Pleaes Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()


