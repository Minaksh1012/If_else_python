service=int(input("Enter the time period of service"))
salary=int(input("Enter your salary"))
if service>5:
    b=5/100*salary
    print("bonus is:",b)
else:
     print("no bonus:",salary)
    
