import csv

with open('data/raw/grocery_prices.csv', newline="") as file:
    reader = csv.DictReader(file)

    cleaned = []

    for row in reader:
    
            row["package_size"] = float(row["package_size"])
            row["regular_price"] = float(row["regular_price"])

            cleaned.append(row)

    with open ('data/processed/grocery_prices_clean.csv', 'w', newline="") as new_file:
        
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        writer.writeheader()

        for row in cleaned:
             writer.writerow(row)