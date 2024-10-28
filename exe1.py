list = [2,3,8,4,6,10,4]

number_validation = 0 

for item in list:
    if item > number_validation:
        number_validation = item
        
print(number_validation)