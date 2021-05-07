for i in range (1,100):
    if i%3==0:
        print("nav")
    elif i%7==0:
        print("gurukul")
    elif i%3==0 and i%7==0:
        print("nav gurukul")
    else:
        print(i)            
