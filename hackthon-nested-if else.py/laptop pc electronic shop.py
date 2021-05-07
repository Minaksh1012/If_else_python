name=input("enter the name")
addres=input("enter the address")
ammount=int(input("enter the purchase ammount"))
type1=input("enter the type of PURCHASE ")
L=0
D=0

if ammount>0 and ammount<25000:
    discount1=0/100*ammount
    discount2=5/100*ammount
if ammount>25001 and ammount<57000:
    discount1=5/100*ammount  
    discount2=7.5/100*ammount
if ammount>57000 and ammount<100000:
    discount1=7.5/100*ammount
    discount2=10/100*ammount
if ammount>100000:
    discount1=10/100*ammount
    discount2=15/100*ammount
netammount1=ammount-discount1
netammount2=ammount-discount2
print("net laptop ammount1:",netammount1)
print("net desktop ammount2:",netammount2)        




