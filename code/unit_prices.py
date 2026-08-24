import csv

rows = []

with open ('data/processed/grocery_prices_clean.csv', newline="") as file:
    reader = csv.DictReader(file)

    fieldnames = reader.fieldnames.copy()
    fieldnames.insert(6, "price_per_oz")

    for row in reader:
        row["package_size"] = float(row["package_size"])
        row["regular_price"] = float(row["regular_price"])
        row["price_per_oz"] = float(round(row["regular_price"] / row["package_size"], 2))

        rows.append(row)

with open ('data/processed/grocery_prices_unit_prices.csv', 'w', newline="") as new_file:

        writer = csv.DictWriter(new_file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(rows)