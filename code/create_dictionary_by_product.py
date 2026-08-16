#Goal is to create a single dictionary with the product types as keys and lists as the value for each key
#and those lists contain row dictionaries

import csv

with open ("data/processed/grocery_prices_unit_prices.csv", newline="") as file:
    reader = csv.DictReader(file)

    dict = {}

    pasta_list = []
    sauce_list = []
    beans_list = []

    for row in reader:
        if row['product_type'] == 'pasta':
            pasta_list.append(row)
        elif row['product_type'] == 'pasta sauce':
            sauce_list.append(row)
        elif row['product_type'] == 'black beans':
            beans_list.append(row)

    dict['pasta'] = pasta_list
    dict['pasta sauce'] = sauce_list
    dict['black beans'] = beans_list

    print(dict)