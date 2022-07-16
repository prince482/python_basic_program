'''
finding the armstrong number between 1 - 500'''

for i in range(1,500):
    sum =0
    temp = i
    while temp > 0:
        last_digit = temp % 10 #finding lAST DIGIT
        sum += last_digit ** 3 
        temp //= 10 #removing last digit
        if i == sum:
            print(i,"is an Armstrong number")