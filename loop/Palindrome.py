'''
Finding the inputed number is palindrome or not
'''
Number = int(input("Enter any 5 digit number"))
temp  = Number
reverse = 0
LAST_NUMBER1 = Number%10
reverse = (reverse*10)+LAST_NUMBER1
INITIAL_NUMBER1= Number//10

LAST_NUMBER2 = INITIAL_NUMBER1%10
reverse = (reverse*10)+LAST_NUMBER2
INITIAL_NUMBER2 = INITIAL_NUMBER1//10

LAST_NUMBER3 = INITIAL_NUMBER2%10
reverse = (reverse*10)+LAST_NUMBER3
INITIAL_NUMBER3 = INITIAL_NUMBER2//10

LAST_NUMBER4 = INITIAL_NUMBER3%10
reverse = (reverse*10)+LAST_NUMBER4
INITIAL_NUMBER4 = INITIAL_NUMBER3//10

LAST_NUMBER5 = INITIAL_NUMBER4%10
reverse = (reverse*10)+LAST_NUMBER5
if(temp == reverse):
    print(f"{Number} is palindrome")
else:
    print(f"{Number} is not a palindrome")