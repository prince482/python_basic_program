'''
find the sum of given series
'''


SUM = 0
for i in range(1,8):
    factorial = 1
    for j in range(1,i+1):
        factorial *= j
    division = i/factorial
    SUM += division
print("Sum of First Seven Terms=", SUM)