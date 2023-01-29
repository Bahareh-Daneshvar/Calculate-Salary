salary=float(input("Enter your salary in Toman: (eg: 70000000)   "))
#tax fee depends on the salary and is some % of salary.it can be see here: https://www.sepidarsystem.com/blog/salary-tax/
if salary<=0:
    print("You entered the wrong number.\nPlease enter a number bigger than Zero for next try ")
    exit(0)
if 0<salary<=7000000:
    tax=0
elif 7000001<salary<14000000:
    tax=(salary-7000000)*10/100
elif 14000001<salary<23000000:
    tax=(salary-14000000)*15/100
elif 23000001<salary<34000000:
    tax=(salary-23000000)*20/100
else:
    tax=(salary-34000000)*30/100
    #I consider the insurance fee equal to 0.5% of the salary
insurance=salary/200
finalsalary=salary-insurance-tax    
print("You monthly income is equal to:  ",finalsalary, "Tomans")

