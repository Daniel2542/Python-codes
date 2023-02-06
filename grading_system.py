#Program to compute students grades
subject1=int(input("Enter marks for the subject:"))
subject2=int(input("Enter marks for the subject:"))
subject3=int(input("Enter marks for the subject:"))
avg=(subject1+subject2+subject3)/3
if(avg>=70 and avg<=100):
    print("Your grade is A")
elif (avg>=60 and avg <=69):
    print("Your grade is B")
elif (avg>=50 and avg <=59):
    print("Your grade is C")
elif (avg>=40 and avg <=49):
    print("Your grade is D")
else:
    print("You Failed")
    
    
