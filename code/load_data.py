import csv

with open('data/raw/grocery_prices.csv', newline="") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        print(row['product_type'], row['store_name'], row['regular_price'])