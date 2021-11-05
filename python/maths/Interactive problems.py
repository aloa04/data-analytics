'''
Interactive problems
'''

# Know the final price of a purchase
# All the products costs 14.99 €
# Non seasonal products have 30% discount
# 1. Ask the user the total number of seasonal and non seasonal products that have brougth
# 2. Obtain the total discount applied
# 3. Tell the user how may products has brougth and how much he has spendt

product:float = 14.99
discount:float = 0.3
seasonal = int(input("Number of seasonal products: "))
non_seasonal = int(input("Number of non seasonal products: "))
total = round ((seasonal*product)+(non_seasonal*product*(1-discount)), 2)
print (" Final price: ", total, "€")
savings = round (((seasonal*product)+(non_seasonal*product))-((seasonal*product)+(non_seasonal*product*(1-discount))), 2)
print ("You have saved: ", savings, "€")