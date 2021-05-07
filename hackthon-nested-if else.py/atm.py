
print("WELCOME TO STATE BANK OF INDIA")
print("password,change_pin,language,balance,withdraw,deposite,exit")
option=int(input("Enter option"))
if option==1:
    
    password=int(input("Enter the password"))
    if password==1234:
        print("password is right:",password) 
    else:
        print("password is wrong")     
if option==2:
    change_pin=int(input("enter the new pin"))
    if change_pin>0:
        print("pin change succesfully")
    else:
        print("invalid pin")
if option==3:
    language=input("enter the language")
    if language=="english" and"marathi" and "hindi":
        print("u choose correct language")
    else:
        print("no language found")    


if option==4:
    balance=int(input("enter the balance"))

    if balance>0:
        print("balance:",balance)
    else:
        print("no balance")    

if option==5:
    balance=int(input("enter the balance"))
    withdraw=int(input("Enter withdraw ammount"))
    forword_balance=balance-withdraw
    print("balance:",balance)
    if withdraw>0:
        print("forward balance:",forword_balance)
    else:
        print("no withdraw made")  

if option==6:
    balance=int(input("enter the balance"))
    deposite=float(input("Enter deposite ammount"))
    if deposite>0:
        forword_balance=balance+deposite
        print("forword balance:",forword_balance)

    else:
        print("no deposite made")

if option==7:
    
   print("exit")