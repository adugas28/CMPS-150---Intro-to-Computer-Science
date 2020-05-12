# Author:         Austin Dugas
# ULID/Section:   C00231110/003
# lab9.py 
 
import math

def AC(radius):
    area = math.pi * radius ** 2
    return area 
 
# WRITE ALL THE OTHER FUNCTIONS 
def AR(length,width):
    area = length * width
    return area

def VC(radius,height):
    volume = math.pi * radius * radius * height
    return volume
 
def VR(length,width,height):
    volume = length * width * height
    return volume

def VS(radius):
    volume = (4/3) * math.pi * radius * radius * radius
    return volume

def SAC(length):
    surfaceArea = 6 * length * length
    return surfaceArea

def SAS(radius):
    surfaceArea = 4 * math.pi * radius * radius
    return surfaceArea

def main():

    infile = open("lab9_input.py","r")

    # get calculation type, but wait on dimension(s) because
    # number of dimensions is dependent on type of shape
    type = (infile.readline()).strip()

    while (type != "###"): 

        if (type == "AC"):
            # read only one dimension for a circle
            radius = float(infile.readline())
            circleArea = AC(radius)
            print(format("Area of a Circle","30s"),format(circleArea,"15.2f"))
 
        # do the processing for all other types of calculations
        elif type == "AR":
            length = float(infile.readline())
            width = float(infile.readline())
            squareArea = AR(length,width)
            print(format("Area of a Rectangle/Square","30s"),
                  format(squareArea,"15.2f"))

        elif type == "VC":
            radius = float(infile.readline())
            height = float(infile.readline())
            cylinderVolume = VC(radius,height)
            print(format("Volume of a Cylinder","30s"),
                  format(cylinderVolume,"15.2f"))

        elif type == "VR":
            length = float(infile.readline())
            width = float(infile.readline())
            height = float(infile.readline())
            rectPrismVol = VR(length,width,height)
            print(format("Volume of a Rectangular Prism","30s"),
                  format(rectPrismVol,"15.2f"))

        elif type == "VS":
            radius = float(infile.readline())
            sphereVolume = VS(radius)
            print(format("Volume of a Sphere","30s"),
                  format(sphereVolume,"15.2f"))

        elif type == "SAC":
            length = float(infile.readline())
            cubeSA = SAC(length)
            print(format("Surface Area of a Cube","30s"),
                  format(cubeSA,"15.2f"))

        elif type == "SAS":
            radius = float(infile.readline())
            sphereSA = SAS(radius)
            print(format("Surface Area of a Sphere","30s"),
                  format(sphereSA,"15.2f"))
 
        # get calculation type, but wait on dimension(s)
        type = (infile.readline()).strip()


    # close the file when you exit the while loop 
    infile.close()
    
main() 
