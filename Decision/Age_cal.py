'''Age calcualtor'''
Ram = int(input("Enter the age of Ram: - "))
Sham = int(input("Enter the age of Sham: - "))
Ajay =int(input("Enter the age of AJAY: - "))
if (Ram < Sham and Ram < Ajay ):
  print("Ram is Younger then Sham and AJAY" )
elif (Sham < Ajay and Sham < Ram ):
  print("Sham is Younger then Ram and AJAY" )
else:
   print(" AJAY is Younger then SHAM and RAM" ) 