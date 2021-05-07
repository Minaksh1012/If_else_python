quantity=int(input("enter the quantity"))
if quantity>=1000:
    discount=quantity*10/100
    cost_price=quantity-discount
    print("cost price of quantity:",cost_price)
    print("discount:",discount)
else:
    print("no discount will give")    