'''
write a program to find a topper in each subject
'''


subjects = ['physics', 'chemistry', 'maths']
physics_marks = []
chemistry_marks = []
maths_marks = []
names = []
for i in range(0,5):
    name = input("Enter the student's name: ")
    physics = int(input("Enter your marks in physics obtained by each student: "))
    chemistry = int(input("Enter your marks in chemistry obtained by each student: "))
    maths = int(input("Enter your marks in maths obtained by each student: "))
    print()
    physics_marks.append(physics)
    chemistry_marks.append(chemistry)
    maths_marks.append(maths)
    names.append(name)
dict_physics = dict(zip(physics_marks,names))
print("\nThe topper of physics:",max([i for i in dict_physics.items()]))
dict_chemistry = dict(zip(chemistry_marks,names))
print("\nThe topper of chemistry :",max([i for i in dict_chemistry.items()]))
dict_maths = dict(zip(maths_marks,names))
print("\nThe topper of math :",max([i for i in dict_maths.items()]))