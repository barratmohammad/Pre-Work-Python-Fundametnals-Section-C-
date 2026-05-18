# inventory.py - A product inventory system for a small store

# Each product is represented as a dictionary with its price and quantity in stock.

inventory = {
    "laptop": {
        "product name": "Laptop",
        "price": 999.99, 
        "quantity": 15
    },
    "mouse": {
        "product name": "Mouse",
        "price": 29.99, 
        "quantity": 50
    },
    "headphones": {
        "product name": "Headphones",
        "price": 199.99, 
        "quantity": 30
    },
    "keyboard": {
        "product name": "Keyboard",
        "price": 49.99, 
        "quantity": 40
    }
    # ... add more
}

def display_inventory():
    """Print the inventory in a formatted way."""
    print("\n" + "=" * 40)
    print ("            Product Inventory")
    print("=" * 40)

    if not inventory:
        print("Product is not in inventory.")
        return
    
    for key, info in inventory.items():
        print(f"\n {info ['product name']}")
        print(f"    Price: {info['price']}")
        print(f"    Quantity: {info['quantity']}")

    print(f"\nTotal products: {len(inventory)}")
    total_value = sum(info['price'] * info['quantity'] for info in inventory.values())
    print(f"Total inventory value: ${total_value:.2f}")
print("=" * 40)

display_inventory()

# Look up a specific product
search = input("\nLook up a product (enter product name): ").lower()

product = inventory.get(search)   # .get() returns None if not found

if product: 
    print(f"\nFound: {product['product name']}")
    print(f"Price: ${product['price']}")
    print(f"Quantity: {product['quantity']}")
else:
    print(f"No product found for '{search}'.")

# Add quantity to an existing product
print("\n--- Update Product Quantity ---")
update_key = input("Enter product name to update quantity: ").lower()
if update_key in inventory:
    additional_qty = int(input("Enter quantity to add: "))
    inventory[update_key]['quantity'] += additional_qty
    print(f"\nUpdated {inventory[update_key]['product name']} quantity to {inventory[update_key]['quantity']}.")
else:
    print(f"Product '{update_key}' not found.") 

# Subtract quantity from an existing product
print("\n--- Subtract Product Quantity ---")
subtract_key = input("Enter product name to subtract quantity: ").lower()
if subtract_key in inventory:
    subtract_qty = int(input("Enter quantity to subtract: "))
    if subtract_qty <= inventory[subtract_key]['quantity']:
        inventory[subtract_key]['quantity'] -= subtract_qty
        print(f"\nUpdated {inventory[subtract_key]['product name']} quantity to {inventory[subtract_key]['quantity']}.")
    else:
        print(f"Cannot subtract {subtract_qty} from {inventory[subtract_key]['product name']} - not enough in stock.")
else:
    print(f"Product '{subtract_key}' not found.")   

display_inventory()

low_stock_threshold = 10
print(f"\nProducts with low stock (less than {low_stock_threshold}):")
for key, info in inventory.items():
    if info['quantity'] < low_stock_threshold:
        print(f" - {info['product name']} (Quantity: {info['quantity']})")  

