'''
creating pant pattern
'''
SPACE = 0
for i in range(71,64,-1): #loop for maintaining rows according to the pattern
    for j in range(65,i+1): #loop for inverted triangle pattern
        print(chr(j), end=" ")
    if SPACE>0: #loop for varying space between letters after each iteration
        for l in range(1,3+(SPACE-1)*4):
            print(end=" ")
    if i<71:
        j=j+1
    for k in range(j-1,64,-1): #loop for reverse inverted triangle pattern
        print(chr(k), end=" ")
    SPACE += 1
    print("")