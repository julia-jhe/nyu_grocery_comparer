#Goal is to create a single dictionary with the product types as keys and lists as the value for each key
#and those lists contain row dictionaries

import csv

with open ("data/processed/grocery_prices_unit_prices.csv", newline="") as file:
    reader = csv.DictReader(file)

    products = {}

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

    products['pasta'] = pasta_list
    products['pasta sauce'] = sauce_list
    products['black beans'] = beans_list

    for product, rows in products.items():
        min_price = 1
        for row in rows:
            if float(row['price_per_oz']) < min_price:
                min_price = float(row['price_per_oz'])
                cheapest_row = row

        print(f"The store with the lowest unit price for {cheapest_row['product_type']} is {cheapest_row['store_name']}, with a regular price of {cheapest_row['regular_price']}, package size of {cheapest_row['package_size']} {cheapest_row['unit']}, and a unit price of {cheapest_row['price_per_oz']}")