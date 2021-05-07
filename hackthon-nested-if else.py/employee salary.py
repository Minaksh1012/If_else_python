print("EMPLOYEE PAYMENT SYSTEM")
basic_salary=int(input("enter the basic salary"))

net_salary=0
gross_pay=0
if dearness_allowance==25/100:
    dearness_allowance==basic_salary*dearness_allowance
    
if house_rent==15/100:
    house_rent=basic_salary*house_rent
        
if provident_fund==8.33/100:
    provident_fund==basic_salary*provident_fund
    
print("dearness allowance:",dearness_allowance)
print("house rent:",house_rent)
print("privident fund:",provident_fund)    
net_salary==basic_salary+dearness_allowance+house_rent
gross_pay==net_salary-provident_fund
print("net salary:",net_salary)
print("gross pay:",gross_pay)    

