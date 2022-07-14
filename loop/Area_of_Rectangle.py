'''
finding which is greater area of 
rectangle of parameter of triangle
'''
length = 5
breadth = 4
area = length*breadth
perimeter = 2*(length+breadth)
print('Area of rectangle=',area)
print('Perimeter of rectangle=',perimeter)
if area>perimeter:
    print('The area of the rectangle is greater than its perimeter.')
else:
    print('The area of the rectangle is smaller than its perimeter.')