#function to find area of circle
def area(rad):
    area=3.142*rad*rad
    return area
rad=int(input("Enter radius of the circle"))
area=area(rad)
print("Area of circle is",area)
        
