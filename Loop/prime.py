'''
finding prime number
'''
FIRST = 1  #first number
LAST = 300 #last number
for Number in range(FIRST,LAST+1):
    if Number > 1: #Prime number starts from 2 and negative numbers are not prime.
        for i in range(2,Number):
            if(Number%i) == 0:
                break
        else:
            print(Number)
