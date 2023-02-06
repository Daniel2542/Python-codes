#program to output employee net bonus
salary=int(input("Enter your salary amount:"))
service_yrs=float(input("Enter number of yrs in service:"))
if(service_yrs>10):
   bonus=salary*0.1
   print("your net bonus amount is:", bonus)
elif (service_yrs>=6 and service_yrs<=10):
    bonus=salary*0.08
    print("your net bonus amount is:", bonus)
else:
    bonus=salary*0.05
    print("your net bonus amount is:", bonus)