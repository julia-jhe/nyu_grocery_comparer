import csv

with open('data/raw/grocery_prices.csv', newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        
        row["package_size"] = float(row["package_size"])
        row["regular_price"] = float(row["regular_price"])

        try:
            row['regular_price'] = float(row['regular_price'])
        except:
            print(f'Invalid price: {row}')