'''
Finding profit and loss
'''
Cost_Price = int(input("Enter the product actual price Rs: - "))
Selling_Price = int(input("Enter the Selling price of the product Rs; - "))
Loss = Cost_Price - Selling_Price
Profit = Selling_Price-Cost_Price
if Selling_Price>Cost_Price:
    print('The seller made the profit of',Profit)
elif Selling_Price == Cost_Price:
    print("The seller donot made any profit")
else:
    print('The seller made the loss of',Loss)
