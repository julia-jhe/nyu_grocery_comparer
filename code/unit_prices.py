import csv

with open ('data/processed/grocery_prices_clean.csv', newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        row["package_size"] = float(row["package_size"])
        row["regular_price"] = float(row["regular_price"])

        price_per_oz = float(round(row["regular_price"] / row["package_size"], 2))
        print(price_per_oz)