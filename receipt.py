# Practice Exercise 3: Receipt Values
item1_name = "Notebook"
item1_price = "4.99"
item1_qty = "2"

item2_name = "Pen Pack"
item2_price = "7.50"
item2_qty = "1"

item3_name = "Backpack"
item3_price = "34.99"
item3_qty = "1"

tax_rate = "0.075" #7.5% sales tax

# Convert string values to appropriate data types for calculations

item1_price = float(item1_price)
item1_qty = int(item1_qty)
item2_price = float(item2_price)
item2_qty = int(item2_qty)
item3_price = float(item3_price)
item3_qty = int(item3_qty)
tax_rate = float(tax_rate)

price = (item1_price * item1_qty) + (item2_price * item2_qty) + (item3_price * item3_qty)

# Display information for formatted introduction

print("=" * 40)
print("              Store Receipt")
print("=" * 40)
print(f"{item1_name}     ${item1_price:.2f} x {item1_qty}        ${item1_price * item1_qty:.2f}")
print(f"{item2_name}     ${item2_price:.2f} x {item2_qty}        ${item2_price * item2_qty:.2f}")
print(f"{item3_name}     ${item3_price:.2f} x {item3_qty}       ${item3_price * item3_qty:.2f}")
print("-" * 40)
print(f"Subtotal:                     ${price:.2f}")
print(f"Tax (7.5%):                          ${price * tax_rate:.2f}")
print("=" * 40)
print(f"Total:                        ${price + (price * tax_rate):.2f}")
print("=" * 40)
