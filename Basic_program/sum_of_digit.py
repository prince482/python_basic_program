'''
SUM of the first and last digit of a NUMBER
'''

NUMBER = int(input('Enter the 4 digit NUMBER= '))
LAST_DIGIT = NUMBER%10
FIRST_DIGIT = NUMBER//1000
SUM = LAST_DIGIT+FIRST_DIGIT
print("The SUM of the first and the last digit of the NUMBER= ", SUM)