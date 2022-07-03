'''
finding area of circle of rectangle
'''
LENGTH_RECTANGLE = int(input("Enter length of rectangle: "))
BREADTH_RECTANGLE = int(input("Enter bredth of rectangle: "))
RADIOUS_OF_CIRCLE = int(input("Enter radious of circle: "))
AREA_OF_RECTANGLE = LENGTH_RECTANGLE*BREADTH_RECTANGLE
PARAMETER_OF_RECTANGLE = 2*(LENGTH_RECTANGLE+BREADTH_RECTANGLE)
AREA_OF_CIRCLE = 2*(3.14*RADIOUS_OF_CIRCLE*RADIOUS_OF_CIRCLE)
CIRCUMFERENCE_OF_CIRCLE = 2*(3.14*RADIOUS_OF_CIRCLE)
print(f"area of rectangel {AREA_OF_RECTANGLE}")
print(f"area of CIRCLE {AREA_OF_CIRCLE}")
print(f"Parameter of rectangel {PARAMETER_OF_RECTANGLE}")
print(f"circumference of circle {CIRCUMFERENCE_OF_CIRCLE}")
