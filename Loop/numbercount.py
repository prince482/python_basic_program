'''
find the count of + -v and 0 number '''
number_1 = int(input("enter how many number you want to input "))
positive = 0
negative = 0
zero = 0
for i in range(0,number_1):
    number_2 = int(input("enter the number "))
    if number_2<0:
     negative = negative+1
    elif number_2>0:
     positive = positive+1
    else:
     zero = zero+1 
print(positive," of nagative number")
print(negative," of Positive number")
print(zero," of Zero number")