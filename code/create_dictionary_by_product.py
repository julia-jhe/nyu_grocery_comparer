#Goal is to create a single dictionary with the product types as keys and lists as the value for each key
#and those lists contain row dictionaries

import csv
import sys

with open ("data/processed/grocery_prices_unit_prices.csv", newline="") as file:
    reader = csv.DictReader(file)

    products = {}

    pasta_list = []
    sauce_list = []
    beans_list = []
    products_list = []

    for row in reader:
        if row['product_type'] == 'pasta':
            pasta_list.append(row)
            products_list.append(row['product_type'])
        elif row['product_type'] == 'pasta sauce':
            sauce_list.append(row)
            products_list.append(row['product_type'])
        elif row['product_type'] == 'black beans':
            beans_list.append(row)
            products_list.append(row['product_type'])

    products['pasta'] = pasta_list
    products['pasta sauce'] = sauce_list
    products['black beans'] = beans_list


    user_product = input("Which product do you wish to look up today?: ")

    if user_product.lower() not in products_list:
        print('Sorry. The item you wish to look up is not in our database.')
        sys.exit()

    for product, rows in products.items():
        if product == user_product.lower():
            min_price = 1
            for row in rows:
                if float(row['price_per_oz']) < min_price:
                        min_price = float(row['price_per_oz'])
                        cheapest_row = row

    print(f"Product: {user_product}\n"
          f"Cheapest store: {cheapest_row['store_name']}\n"
          f"Regular price: ${cheapest_row['regular_price']}\n"
          f"Package size: {cheapest_row['package_size']} {cheapest_row['unit']}\n"
          f"Unit price: ${cheapest_row['price_per_oz']}\n")


    additional_info = input("Do you wish to see additional information about this product at this store?: ")

    if additional_info.lower() == 'yes':
        if cheapest_row['notes'] == '':
            print(f"Product details: {cheapest_row['product_details']}\n"
                  f"Brand: {cheapest_row['brand']}\n"
                  f"Store location: {cheapest_row['store_location']}\n"
                  "Notes: none\n")
        else:
            print(f"Product details: {cheapest_row['product_details']}\n"
                  f"Brand: {cheapest_row['brand']}\n"
                  f"Store location: {cheapest_row['store_location']}\n"
                  f"Notes: {cheapest_row['notes']}\n")
    else:
        print('Thank you for using this service. Have a nice day.')