'''
calculating gross salary
'''
ENGISH = int(input("Enter the makrs of english: "))
HINDI = int(input("Enter the makrs of hindi: "))
SCIENCE = int(input("Enter the makrs of science: "))
MATH = int(input("Enter the makrs of math: "))
HISTORY = int(input("Enter the makrs of history: "))
TOTAL_MARKS = 500
MARKS_OBTAINED = ENGISH+HINDI+SCIENCE+MATH+HISTORY
PERSENTAGE = MARKS_OBTAINED/TOTAL_MARKS*100
if TOTAL_MARKS < MARKS_OBTAINED:
    print(" The number you have inputted is not correct")
else:
    print(f"Total Marks = {TOTAL_MARKS}")
    print(f"MARKS OBTAINED = {MARKS_OBTAINED}")
    print(f"PERSENTAGE= {PERSENTAGE}")
