pr=int(input("enter the cost price of bike"))
tax=0
if  pr>100000:
    tax=15/100* pr
elif  pr>500000 and  pr<=100000:
    tax=10/100* pr
else:
    tax=5/100* pr
    print("tax to be paid",tax)        