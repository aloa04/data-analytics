'''
Simple math problems
'''
# 1. Math - ((6-2)/2)^2
# 2. Round to 2 decimals
result:float = (((6-2)/5))**2
print (result)
print (round(result))
print (round(result, 4))
print (result.__round__(4))

# 1. Obtain invest result
capital = 45000
interest = 15
years = 20
result_invest:float = (capital * ( 1 + (interest/100)) ** years)
print(round(result_invest, 4))