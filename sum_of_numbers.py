'''
Total sum of integers
'''

NUMBER = int(input("Enter the number: "))
SUM_OF_INPUT = 0
LAST_NUMBER = NUMBER%10 # To get the last number
SUM_OF_INPUT= LAST_NUMBER+ SUM_OF_INPUT
NUMBER = NUMBER//10 # TO erase the last number

LAST_NUMBER = NUMBER%10 # To get the last number
SUM_OF_INPUT= LAST_NUMBER+ SUM_OF_INPUT
NUMBER = NUMBER//10 # TO erase the last number

LAST_NUMBER = NUMBER%10 # To get the last number
SUM_OF_INPUT= LAST_NUMBER+ SUM_OF_INPUT
NUMBER = NUMBER//10 # TO erase the last number

LAST_NUMBER = NUMBER%10 # To get the last number
SUM_OF_INPUT= LAST_NUMBER+ SUM_OF_INPUT
NUMBER = NUMBER//10 # TO erase the last number

LAST_NUMBER = NUMBER%10 # To get the last number
SUM_OF_INPUT= LAST_NUMBER+ SUM_OF_INPUT
NUMBER = NUMBER//10 # TO erase the last number
print(f"TOTAL sum of = {SUM_OF_INPUT}") 
    


    