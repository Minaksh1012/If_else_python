ammount=int(input("enter the ammount"))
if ammount<2000:
    discount=5/100
elif ammount>2001 and ammount<5000:
    discount=25/100
elif ammount>5001 and ammount<10000:
    discount=35/100
elif ammount>10000:
    discount=50/100
discount=discount*ammount 
print("discount:",discount) 
  
cost_price=ammount-discount
print("total cost price:",cost_price)                
