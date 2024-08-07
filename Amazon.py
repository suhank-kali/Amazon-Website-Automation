import tagui as t
import pandas as pd

# Define the search term
search_term = "smartphone"

# Start TagUI
t.init()

# Go to Amazon website
t.url('https://www.amazon.in/')

# Search for the item
t.type('input[name="field-keywords"]', search_term + '[enter]')

# Wait for results to load
t.wait(5)

# Scrape the product names and prices
products = []
for i in range(1, 20):  # Adjust the range for more items
    try:
        name_selector = f'(//span[@class="a-size-medium a-color-base a-text-normal"])[{i}]'
        price_selector = f'(//span[@class="a-price-whole"])[{i}]'
        
        name = t.read(name_selector)
        price = t.read(price_selector)

        products.append({'Product Name': name, 'Price': price})
    except:
        continue

# Convert to DataFrame
df = pd.DataFrame(products)

# Save to Excel
df.to_excel('amazon_search_results.xlsx', index=False)

# Close TagUI
t.close()


