bank_name=input("enter the bank name")
card=input("enter the card name")
if card=="debit card"or card=="credit card":
    print("u select valid card")
    pin=int(input("enter the pin"))
    change_pin=int(input("enter the new pin"))
    if pin==1234:
        print("valid pin")    
    if change_pin>0:
        print("your pin has been successfully changed")
        balance=int(input("enter the balance"))
        if balance>0:
            print("u have sufficient balance")
            withdraw=int(input("enter the withdraw ammount"))
            if withdraw>0:
                print("withdraw successful")
                transaction=int(input("enter the transaction ammount"))
                if transaction>0:
                    print("your transaction successful")
                    deposite=int(input("enter the deposite ammount"))
                    if deposite>0:
                        print("deposite successfully")
                        sleep=input("do want sleep")
                        if sleep=="yes":
                            print("take sleep")
                        else:
                            print("exit")    

                    else:
                            print("unsuccesful")
                else:
                        print("transaction successful")
            else:
                    print("no ammount to withdraw")
        else:
                print("no balance")                     
    else:
            print("entered valid pin to proceed")               
else:
    print("invalid card")            