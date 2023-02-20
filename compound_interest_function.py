# Python program to find compound interest 
 
def compound_interest(principal, rate, time):
    Amount = principal * (pow((1 + rate / 100), time))
    C_interest = Amount - principal
principal=int(input("Enter principal amount:"))
rate=int(input("Enter rate:"))
time=int(input("Enter time:"))
Amount = principal * (pow((1 + rate / 100), time))
C_interest = Amount - principal
print("The compound interest is", C_interest)
    
