'''
valid triangle or not
'''
Angle1 = int(input("Enter the first angle of triangle "))
Angle2 = int(input("Enter the second angle of triangle "))
Angle3 = int(input("Enter the thiird angle of triangle "))
sum = Angle1+Angle2+Angle3
if sum == 180 :
    print("It is a valid triangle")
else:
    print("It is not a valid triangle")