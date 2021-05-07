water=int(input("enter the quantity of water"))
if water>45 and water<75:
    print("tax rate is 475 rs")
elif water >75 and water<125:
    print("tax rate is 750 rs")
elif water>125 and water<200:
    print("tax rate is 1225 rs")
elif water>200 and water<350:
    print("tax rate is 1650 rs")
elif water>350:
    print("tax rate is 2000 rs")                