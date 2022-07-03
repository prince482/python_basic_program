'''
basic salary
'''
BASI_SALARY = int(input("Enter the basic salary: "))
DEARNESS = (BASI_SALARY*60)/100
RENT = (BASI_SALARY*20)/100
GROSS_SALARY = BASI_SALARY+DEARNESS+RENT
print(f"Basic salary ={BASI_SALARY}")
print(f"DEARNESS allowance = {DEARNESS}")
print(f"RENT allowance = {RENT}")
print(f"Gross Salary = {GROSS_SALARY}")