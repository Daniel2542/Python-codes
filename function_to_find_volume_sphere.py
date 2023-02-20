#function to find volume of sphere
def volume_of_sphere(rad):
    volume=4/3*3.142*rad*rad*rad
    return volume
rad=int(input("Enter radius of the sphere:"))
volume=volume_of_sphere(rad)
print("The volume of the cylinder is:", volume)
