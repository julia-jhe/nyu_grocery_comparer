# Data Collection Method

This document records the data collection and comparison methodology used for v1.0.0.


## Region

Grocery stores within walking distance of NYU's Washington Square Campus.


## Stores (3)

- Morton Williams
- Trader Joe's
- Whole Foods Market


## Products (3)

- Pasta
- Pasta sauce
- Black beans


## Information Collected

- Store name
- Product type
- Product details
- Package size
- Unit
- Regular price
- Collection date
- Brand
- Store location
- Source (URL) 
- Notes (if any)


## Collection Rules

Only regular (non-membership) prices were collected in v1.0.0. All prices were collected within the same general time period. 

For each product at each store, the closest comparable item was selected. Product type and basic product characteristics, including size, unit, and product details, were matched as closely as possible across stores. Brand and bestseller status did not determine which item was selected.

Package size and item price were used to calculate a unit price, allowing items with slightly different package sizes to be compared equally. 

Product details, brand, and store location were recorded for transparency but did not affect ranking.

If no item met the preferred comparison criteria, the closest reasonable match was selected and any differences were recorded in the 'notes' column. If no reasonably comparable item was available, the product was recorded as unavailable. 

For each product type, stores were compared based on the calculated unit price. The store with the lowest calculated unit price was identified as the cheapest option for that product. 

## Data Storage

Raw data collected was initially recorded in a Google Sheets document. Each row represents one specific product at one store. 

The data used by the Python program was converted into CSV format from the Google Sheets document. 