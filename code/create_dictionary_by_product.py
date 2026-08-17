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


    user_product = input("Which product do you wish to look up today?: ")

    for product, rows in products.items():
        if product == user_product:
            min_price = 1
            for row in rows:
                if float(row['price_per_oz']) < min_price:
                        min_price = float(row['price_per_oz'])
                        cheapest_row = row

    print(f"The store with the lowest unit price for {user_product} is {cheapest_row['store_name']}, with a regular price of {cheapest_row['regular_price']}, package size of {cheapest_row['package_size']} {cheapest_row['unit']}, and a unit price of {cheapest_row['price_per_oz']}")


    additional_info = input("Do you wish to see additional product information?: ")

    if additional_info == 'Yes':
        if cheapest_row['notes'] == '':
            print(f"Product details: {cheapest_row['product_details']}. Brand: {cheapest_row['brand']}. Store location: {cheapest_row['store_location']}. Notes: none")
        else:
            print(f"Product details: {cheapest_row['product_details']}. Brand: {cheapest_row['brand']}. Store location: {cheapest_row['store_location']}. Notes: {cheapest_row['notes']}")
    else:
        print('Thank you for using this service. Have a nice day.')