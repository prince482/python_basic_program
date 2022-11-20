'''
Program to find the item in that budget
'''

item = []
prices = [10,20,900]
for i in range(0, 3):
    elements = input("\nEnter item name: ")
    item.append(elements) #.append is used to insert the item in a list.
items = dict(zip(prices,item))
budget = int(input("\nEnter your budget="))
print("\nList of items which are under your budget:",[items[i] for i in items if i <= budget])