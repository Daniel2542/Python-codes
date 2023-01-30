amount=float(input("Enter the amount "))
if(amount > 1000 ):
    discount=0.05*1000
    newamount=amount-discount
    print("The new amount is ",newamount)
    print("The discount is ",discount)
    
else:
    print("The amount is",amount)
