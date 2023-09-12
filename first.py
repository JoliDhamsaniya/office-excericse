class Category:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.no_of_products = 0

    def __str__(self):
        return f"Category Name: {self.name}, Category Code: {self.code}, No. of Products: {self.no_of_products}"

class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price

    def __str__(self):
        return f"Product Name: {self.name}, Product Code: {self.code}, Category: {self.category}, Price: {self.price}"

# Create three category objects
category1 = Category("Electronics", "E001")
category2 = Category("Clothing", "C002")
category3 = Category("Books", "B003")

# Create 10 different product objects with unique codes
products = [
    Product("Laptop", "P001", category1, 999.99),
    Product("Smartphone", "P002", category1, 499.99),
    Product("T-shirt", "P003", category2, 19.99),
    Product("Jeans", "P004", category2, 39.99),
    Product("Novel", "P005", category3, 9.99),
    Product("Tablet", "P006", category1, 299.99),
    Product("Dress", "P007", category2, 49.99),
    Product("Shoes", "P008", category2, 29.99),
    Product("Cookbook", "P009", category3, 14.99),
    Product("Headphones", "P010", category1, 49.99)
]

# Update the no_of_products for each category
for Product in products:
    Product.category.no_of_products += 1

# Print category info with its no_of_products
for category in [category1, category2, category3]:
    print(category)

# Sort and print products based on price (Price High to Low)
sorted_products_high_to_low = sorted(products, key=lambda x: x.price, reverse=True)
print("\nProducts Sorted by Price (High to Low):")
for product in sorted_products_high_to_low:
    print(product)

# Sort and print products based on price (Price Low to High)
sorted_products_low_to_high = sorted(products, key=lambda x: x.price)
print("\nProducts Sorted by Price (Low to High):")
for product in sorted_products_low_to_high:
    print(product)

# Search for a product using its code
search_code = "P003"
found_product = next((product for product in products if product.code == search_code), None)
if found_product:
    print(f"\nProduct Found: {found_product}")
else:
    print(f"\nProduct with code '{search_code}' not found.")
