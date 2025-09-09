systemMenu = {"ข้าวผัด":45,"ข้าวไข่เจียว":40,"ข้าวราดแกง":50,"ข้าวหน้าไก่":45}
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

        menuList.append([menuName,systemMenu[menuName]])
showBill()
