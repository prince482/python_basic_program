''' write a program that will be used to take a new name at new index
if user input a name which already exists in the list the name will 
eenot be added and will show the previous list '''

__author__ = "Shakir Sadiq"

name = ['Thor','black panther']
print("list of names:", name)
for i in range(0,3):
    i = input("Enter a name: ")
    if i not in name:
        name.append(i)
        print(name)
    else:
        print(name)