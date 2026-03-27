#exercise
sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

# 1. Total Sales Calculation & 3. Sales Data Enhancement
# We can do these in one pass to be efficient!
category_sales = {}
customer_spending = {}

for transaction in sales_data:
    # Calculate total price for this transaction
    line_total = transaction["price"] * transaction["quantity"]
    transaction["total_price"] = line_total # Task 3: Enhancement
    
    # Task 1: Category totals
    prod = transaction["product"]
    category_sales[prod] = category_sales.get(prod, 0) + line_total
    
    # Task 2: Customer Spending Profile
    c_id = transaction["customer_id"]
    customer_spending[c_id] = customer_spending.get(c_id, 0) + line_total

# 4. High-Value Transactions (> $500)
# Using list comprehension and then sorting
high_value_tx = [t for t in sales_data if t["total_price"] > 500]
high_value_tx.sort(key=lambda x: x["total_price"], reverse=True)

# 5. Customer Loyalty Identification
purchase_counts = {}
for t in sales_data:
    c_id = t["customer_id"]
    purchase_counts[c_id] = purchase_counts.get(c_id, 0) + 1

loyal_customers = [c_id for c_id, count in purchase_counts.items() if count > 1]

# --- Bonus: Insights ---
# Most Popular Product
popularity = {}
for t in sales_data:
    popularity[t["product"]] = popularity.get(t["product"], 0) + t["quantity"]
most_popular = max(popularity, key=popularity.get)

# Display Results
print(f"Total Sales by Category: {category_sales}")
print(f"Customer Spending: {customer_spending}")
print(f"Loyal Customer IDs: {loyal_customers}")
print(f"Most Popular Product: {most_popular}")