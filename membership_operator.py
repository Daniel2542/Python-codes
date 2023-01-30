countries=["Kenya","Uganda", "Tanzania"]
country=(input("Enter your country"))
age=int(input("Enter your age"))
if ((age>=18)and(country in countries)):
    print("You are allowed to vote")
 else:
    print("You are not allowed to vote")   