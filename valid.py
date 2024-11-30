'''author:aishwarya'''
def check_rightangle(side1,side2,side3):
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2:
         return True
    return False

side1=int(input("enter the first side"))
side2=int(input("enter the second side"))
side3=int(input("enter the third side"))
if check_rightangle(side1,side2,side3):
    print(f"the given sides are part of right angle")
else:
    print(f"the given sides are not part of right angle triangle")