'''
Carting a program where number will be updated at the even places
'''

MY_list = [12,45,56,78,65,546,12]
for i in range(0,6,2):
    MY_list[i] = MY_list[i]+1
for i in range(1,7,2):
    MY_list[i] = MY_list[i]+2
print(MY_list)