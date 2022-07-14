'''
program to find leap year or not
'''
Year = int(input("Enter the Year"))
if((Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year")
  # Else it is not a leap year  
else:  
    print ("Given Year is not a leap Year")  