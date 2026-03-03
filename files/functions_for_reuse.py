# functions_for_reuse.py
# 
# This file contains 16 functions from Assignment 2 plus 3 NEW/UPDATED functions for Assignment 3.
# Your task: organize these functions into the appropriate modules for Assignment 3.
#
# Instructions:
# 1. Create three new files: main.py (rename given template), 
#    data_handler.py, inventory_operations.py
# 2. Read each function below and decide which module it belongs in
# 2. Copy all 19 functions to appropriate modules as-is (NO changes needed - all A3-ready)
# 4. Add any necessary import statements to each module
# 5. Write 7 NEW file operation functions
#
# Remember: Ask yourself "What is this function's job?" to decide where it goes:
#   - Talking to files? → data_handler.py
#   - Processing inventory data? → inventory_operations.py  
#   - Showing menus or getting user input? → main.py
#
# DO NOT submit this file - it is just for organizing your code.

from datetime import datetime


# =============================================================================
# FUNCTION 1
# =============================================================================

def get_valid_float(prompt, min_value=0.0):
    """
    Prompt the user for a float value and validate it.
    
    Parameters:
        prompt (str): The message to display to the user
        min_value (float): The minimum acceptable value (default: 0.0)
    
    Returns:
        float: A valid float value >= min_value
    """
    while True:
        try:
            value = float(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Error: Value must be at least {min_value}")
        except ValueError:
            print("Error: Please enter a valid number")


# =============================================================================
# FUNCTION 2
# =============================================================================

def get_valid_int(prompt, min_value=0):
    """
    Prompt the user for an integer value and validate it.
    
    Parameters:
        prompt (str): The message to display to the user
        min_value (int): The minimum acceptable value (default: 0)
    
    Returns:
        int: A valid integer value >= min_value
    """
    while True:
        try:
            value = int(input(prompt))
            if value >= min_value:
                return value
            else:
                print(f"Error: Value must be at least {min_value}")
        except ValueError:
            print("Error: Please enter a valid whole number")


# =============================================================================
# FUNCTION 3
# =============================================================================

def generate_product_id(inventory):
    """
    Generate the next unique product ID (P001, P002, P003, etc.).
    
    Parameters:
        inventory (dict): The inventory dictionary with product IDs as keys
    
    Returns:
        str: Next product ID in format P001, P002, etc.
    """
    if not inventory:
        return "P001"
    
    # Extract all numeric parts from existing IDs
    max_num = 0
    for product_id in inventory.keys():
        # Extract number from "P001" format
        num = int(product_id[1:])
        if num > max_num:
            max_num = num
    
    # Generate next ID
    next_num = max_num + 1
    return f"P{next_num:03d}"


# =============================================================================
# FUNCTION 4
# =============================================================================

def find_product_by_name(inventory, search_term):
    """
    Search for products whose name contains the search term (case-insensitive).
    
    Parameters:
        inventory (dict): The inventory dictionary
        search_term (str): The term to search for
    
    Returns:
        list: List of (product_id, product_dict) tuples matching the search
    """
    matches = []
    search_lower = search_term.lower()
    
    for product_id, product in inventory.items():
        if search_lower in product["name"].lower():
            matches.append((product_id, product))
    
    return matches


# =============================================================================
# FUNCTION 5
# =============================================================================

def find_product_by_category(inventory, category):
    """
    Find all products in a specific category (case-insensitive exact match).
    
    Parameters:
        inventory (dict): The inventory dictionary
        category (str): The category to search for
    
    Returns:
        list: List of (product_id, product_dict) tuples in the category
    """
    matches = []
    category_lower = category.lower()
    
    for product_id, product in inventory.items():
        if product["category"].lower() == category_lower:
            matches.append((product_id, product))
    
    return matches


# =============================================================================
# FUNCTION 6
# =============================================================================

def log_transaction(transactions, trans_type, product_id, product_name, quantity):
    """
    Log a transaction (sale, delivery, or product addition).
    
    Parameters:
        transactions (list): The list of transaction dictionaries
        trans_type (str): Type of transaction ("sale", "delivery", or "added")
        product_id (str): The product ID involved
        product_name (str): The product name
        quantity (int): The quantity (negative for sales, positive for deliveries/additions)
    """
    transaction = {
        "type": trans_type,
        "product_id": product_id,
        "product_name": product_name,
        "quantity": quantity,
        "timestamp": datetime.now().isoformat()
    }
    transactions.append(transaction)


# =============================================================================
# FUNCTION 7
# =============================================================================

def view_transaction_log(transactions, num_recent=10):
    """
    Display recent transactions from the log.
    
    Parameters:
        transactions (list): The list of transaction dictionaries
        num_recent (int): Number of recent transactions to display (default: 10)
    """
    print(f"\n--- Transaction Log (Last {num_recent}) ---")
    
    if not transactions:
        print("No transactions recorded yet.")
        return
    
    # Display header
    print(f"{'Timestamp':<20} {'Type':<10} {'Product':<20} {'Quantity':<10}")
    print("=" * 60)
    
    # Show most recent transactions
    recent = transactions[-num_recent:] if len(transactions) > num_recent else transactions
    
    for trans in reversed(recent):  # Show newest first
        # Parse timestamp to make it more readable
        timestamp = datetime.fromisoformat(trans["timestamp"])
        time_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        
        # Format quantity with sign
        qty_str = f"{trans['quantity']:+d}" if trans['type'] != 'added' else str(trans['quantity'])
        
        print(f"{time_str:<20} {trans['type'].capitalize():<10} "
              f"{trans['product_name']:<20} {qty_str:<10}")
    
    print("=" * 60)


# =============================================================================
# FUNCTION 8
# =============================================================================

def view_all_products(inventory):
    """
    Display all products in the inventory in a formatted table.
    
    Parameters:
        inventory (dict): The inventory dictionary with product IDs as keys
    """
    print("\n--- All Products ---")
    
    if not inventory:
        print("No products in inventory.")
        return
    
    # Print table header
    print(f"{'ID':<6} {'Product':<20} {'Category':<15} {'Price':<10} {'Stock':<10} {'Min Stock':<10}")
    print("=" * 71)
    
    # Print each product
    for product_id, product in inventory.items():
        print(f"{product_id:<6} {product['name']:<20} {product['category']:<15} "
              f"€{product['price']:<9.2f} {product['quantity']:<10} {product['min_stock']:<10}")
    
    print("=" * 71)
    print(f"Total products: {len(inventory)}")


# =============================================================================
# FUNCTION 9
# =============================================================================

def add_product(inventory, transactions):
    """
    Add a new product to the inventory after checking for duplicates.
    
    Parameters:
        inventory (dict): The inventory dictionary
        transactions (list): The transactions list for logging
    
    Returns:
        str or None: Product ID if successful, None if duplicate found
    """
    print("\n--- Add New Product ---")
    
    # Get product name and check for duplicates (case-insensitive)
    name = input("Enter product name: ").strip()
    
    # Check if name already exists
    for product in inventory.values():
        if product["name"].lower() == name.lower():
            print(f"Error: Product '{name}' already exists in inventory.")
            return None
    
    # Get remaining product details with validation
    category = input("Enter category: ").strip()
    price = get_valid_float("Enter price (€): ", min_value=0.01)
    qty = get_valid_int("Enter current stock quantity: ", min_value=0)
    min_stock = get_valid_int("Enter minimum stock level: ", min_value=0)
    
    # Generate unique product ID
    product_id = generate_product_id(inventory)
    
    # Create new product dictionary
    new_product = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": qty,
        "min_stock": min_stock
    }
    
    # Add to inventory
    inventory[product_id] = new_product
    
    # Log the transaction
    log_transaction(transactions, "added", product_id, name, qty)
    
    print(f"\nProduct '{name}' added successfully with ID: {product_id}")
    return product_id


# =============================================================================
# FUNCTION 10
# =============================================================================

def update_stock(inventory, transactions):
    """
    Update the stock quantity for a product (sale or delivery).
    
    Parameters:
        inventory (dict): The inventory dictionary
        transactions (list): The transactions list for logging
    
    Returns:
        bool: True if stock was updated successfully, False otherwise
    """
    print("\n--- Update Stock ---")
    
    # Get product name to update
    name = input("Enter product name: ").strip()
    
    # Find the product
    product_id = None
    product = None
    for pid, prod in inventory.items():
        if prod["name"].lower() == name.lower():
            product_id = pid
            product = prod
            break
    
    if product is None:
        print(f"Error: Product '{name}' not found in inventory.")
        return False
    
    # Ask whether it's a sale or delivery
    transaction_type = input("Is this a (S)ale or (D)elivery? ").strip().lower()
    
    while transaction_type not in ['s', 'd', 'sale', 'delivery']:
        print("Error: Please enter 'S' for sale or 'D' for delivery")
        transaction_type = input("Is this a (S)ale or (D)elivery? ").strip().lower()
    
    # Get quantity
    quantity = get_valid_int("Enter quantity: ", min_value=1)
    
    # Process sale
    if transaction_type in ['s', 'sale']:
        if product["quantity"] < quantity:
            print(f"Error: Insufficient stock. Only {product['quantity']} units available.")
            return False
        product["quantity"] -= quantity
        log_transaction(transactions, "sale", product_id, product["name"], -quantity)
        print(f"\nStock updated! {product['name']} now has {product['quantity']} units.")
    
    # Process delivery
    else:  # delivery
        product["quantity"] += quantity
        log_transaction(transactions, "delivery", product_id, product["name"], quantity)
        print(f"\nStock updated! {product['name']} now has {product['quantity']} units.")
    
    return True


# =============================================================================
# FUNCTION 11
# =============================================================================

def update_product_details(inventory):
    """
    Update product details (name, category, price, min_stock) for an existing product.
    
    Note: Quantity is updated through update_stock() to maintain transaction log.
    
    Parameters:
        inventory (dict): The inventory dictionary
    
    Returns:
        bool: True if updated successfully, False if product not found
    """
    print("\n--- Update Product Details ---")
    
    # Get product name to update
    name = input("Enter product name: ").strip()
    
    # Find the product
    product_id = None
    product = None
    for pid, prod in inventory.items():
        if prod["name"].lower() == name.lower():
            product_id = pid
            product = prod
            break
    
    if product is None:
        print(f"Error: Product '{name}' not found in inventory.")
        return False
    
    # Show current details
    print(f"\nCurrent details for '{product['name']}' ({product_id}):")
    print(f"Name: {product['name']}")
    print(f"Category: {product['category']}")
    print(f"Price: €{product['price']:.2f}")
    print(f"Minimum stock: {product['min_stock']}")
    
    # Get new values (allow keeping current by pressing Enter or entering -1)
    print("\nEnter new values (press Enter to keep current):")
    
    new_name = input("Enter new name (or press Enter to keep current): ").strip()
    if new_name:
        # Check if new name conflicts with existing products
        for other_pid, other_prod in inventory.items():
            if other_pid != product_id and other_prod["name"].lower() == new_name.lower():
                print(f"Error: Product name '{new_name}' already exists.")
                return False
        product["name"] = new_name
    
    new_category = input("Enter new category (or press Enter to keep current): ").strip()
    if new_category:
        product["category"] = new_category
    
    print("Enter new price (or -1 to keep current): ", end='')
    new_price = get_valid_float("", min_value=-1.0)
    if new_price > 0:
        product["price"] = new_price
    
    print("Enter new minimum stock (or -1 to keep current): ", end='')
    new_min = get_valid_int("", min_value=-1)
    if new_min >= 0:
        product["min_stock"] = new_min
    
    print("\nProduct details updated successfully!")
    return True


# =============================================================================
# FUNCTION 12
# =============================================================================

def remove_product(inventory):
    """
    Remove a product from the inventory after confirmation.
    
    Parameters:
        inventory (dict): The inventory dictionary
    
    Returns:
        bool: True if product was removed successfully, False otherwise
    """
    print("\n--- Remove Product ---")
    
    # Get product name to remove
    name = input("Enter product name: ").strip()
    
    # Find the product
    product_id = None
    product = None
    for pid, prod in inventory.items():
        if prod["name"].lower() == name.lower():
            product_id = pid
            product = prod
            break
    
    if product is None:
        print(f"Error: Product '{name}' not found in inventory.")
        return False
    
    # Confirm deletion
    confirm = input(f"Are you sure you want to remove '{product['name']}'? (Y/N): ").strip().lower()
    
    if confirm == 'y' or confirm == 'yes':
        del inventory[product_id]
        print(f"\nProduct '{name}' removed successfully!")
        return True
    else:
        print("Removal cancelled.")
        return False


# =============================================================================
# FUNCTION 13
# =============================================================================

def search_products(inventory):
    """
    Search for products by name or category and display results.
    
    Parameters:
        inventory (dict): The inventory dictionary
    """
    print("\n--- Search Products ---")
    
    # Ask search type
    search_type = input("Search by (N)ame or (C)ategory? ").strip().lower()
    
    while search_type not in ['n', 'c', 'name', 'category']:
        print("Error: Please enter 'N' for name or 'C' for category")
        search_type = input("Search by (N)ame or (C)ategory? ").strip().lower()
    
    # Perform appropriate search
    if search_type in ['n', 'name']:
        search_term = input("Enter search term: ").strip()
        matches = find_product_by_name(inventory, search_term)
    else:  # category
        category = input("Enter category: ").strip()
        matches = find_product_by_category(inventory, category)
    
    # Display results
    print("\n--- Search Results ---")
    
    if not matches:
        print("No products found matching your search.")
        return
    
    # Print table header
    print(f"{'ID':<6} {'Product':<20} {'Category':<15} {'Price':<10} {'Stock':<10}")
    print("=" * 61)
    
    # Print each matching product
    for product_id, product in matches:
        print(f"{product_id:<6} {product['name']:<20} {product['category']:<15} "
              f"€{product['price']:<9.2f} {product['quantity']:<10}")
    
    print("=" * 61)
    print(f"Found {len(matches)} product(s)")


# =============================================================================
# FUNCTION 14
# =============================================================================

def view_low_stock(inventory):
    """
    Display products that are at or below their minimum stock level.
    
    Parameters:
        inventory (dict): The inventory dictionary
    """
    print("\n--- Low Stock Alerts ---")
    
    # Find products with low stock
    low_stock_products = []
    for product_id, product in inventory.items():
        if product["quantity"] <= product["min_stock"]:
            low_stock_products.append((product_id, product))
    
    if not low_stock_products:
        print("No products currently below minimum stock level.")
        return
    
    # Display low stock products
    print(f"{'ID':<6} {'Product':<20} {'Category':<15} {'Current':<10} {'Minimum':<10} {'Order':<10}")
    print("=" * 71)
    
    for product_id, product in low_stock_products:
        order_qty = product["min_stock"] - product["quantity"] + product["min_stock"]  # Reorder to double min
        print(f"{product_id:<6} {product['name']:<20} {product['category']:<15} "
              f"{product['quantity']:<10} {product['min_stock']:<10} {order_qty:<10}")
    
    print("=" * 71)
    print(f"Total products needing reorder: {len(low_stock_products)}")


# =============================================================================
# FUNCTION 15
# =============================================================================

def generate_category_report(inventory):
    """
    Generate a report showing product count and total value per category.
    
    Parameters:
        inventory (dict): The inventory dictionary
    
    Returns:
        dict: Dictionary mapping category to {"count": n, "value": v}
    """
    print("\n--- Category Report ---")
    
    if not inventory:
        print("No products in inventory.")
        return {}
    
    # Build category summary
    category_data = {}
    
    for product in inventory.values():
        category = product["category"]
        product_value = product["price"] * product["quantity"]
        
        if category not in category_data:
            category_data[category] = {"count": 0, "value": 0.0}
        
        category_data[category]["count"] += 1
        category_data[category]["value"] += product_value
    
    # Display report
    print(f"{'Category':<20} {'Products':<12} {'Total Value':<15}")
    print("=" * 47)
    
    total_products = 0
    total_value = 0.0
    
    for category, data in sorted(category_data.items()):
        print(f"{category:<20} {data['count']:<12} €{data['value']:<14.2f}")
        total_products += data["count"]
        total_value += data["value"]
    
    print("=" * 47)
    print(f"{'Total:':<20} {total_products:<12} €{total_value:<14.2f}")
    
    return category_data


# =============================================================================
# FUNCTION 16
# =============================================================================

def calculate_inventory_value(inventory):
    """
    Calculate the total value of all inventory (price × quantity).
    
    Parameters:
        inventory (dict): The inventory dictionary
    
    Returns:
        float: Total inventory value
    """
    print("\n--- Total Inventory Value ---")
    
    if not inventory:
        print("No products in inventory.")
        return 0.0
    
    total = 0.0
    for product in inventory.values():
        product_value = product["price"] * product["quantity"]
        total += product_value
    
    print(f"Total inventory value: €{total:.2f}")
    return total


# =============================================================================
# FUNCTIONS 17-18: A3-READY VERSIONS (Copy as-is)
# =============================================================================

# =============================================================================
# FUNCTION 17 - A3-READY VERSION
# =============================================================================

def display_menu():
    """
    Display the main menu and return the user's validated choice.
    
    A3 VERSION - Updated for 11 options with Export Reports and Save & Exit.
    
    Returns:
        int: The user's menu choice (1-11)
    """
    print("\n=== Murphy's General Store - Inventory System ===")
    print("1. View All Products")
    print("2. Add New Product")
    print("3. Update Stock (Sale/Delivery)")
    print("4. Update Product Details")
    print("5. Remove Product")
    print("6. Search Products")
    print("7. View Low Stock Alerts")
    print("8. View Category Report")
    print("9. View Transaction Log")
    print("10. Export Reports")
    print("11. Save & Exit")
    
    choice = get_valid_int("\nEnter your choice (1-11): ", min_value=1)
    
    while choice > 11:
        print("Error: Please enter a number between 1 and 11")
        choice = get_valid_int("Enter your choice (1-11): ", min_value=1)
    
    return choice


# =============================================================================
# FUNCTION 18 - A3-READY VERSION
# =============================================================================

def main():
    """
    Main programme loop with persistent storage.
    
    A3 VERSION - Includes file loading, export submenu, and data saving.
    """
    # Welcome message
    print("\nWelcome to Murphy's General Store Inventory System!")
    
    # Load data from files (add filename parameters)
    inventory = load_inventory()
    transactions = load_transactions()
    
    # Display load results
    print(f"Loaded {len(inventory)} products from inventory.json")
    print(f"Loaded {len(transactions)} transactions from transactions.json")
    
    # Main menu loop
    while True:
        choice = display_menu()
        
        if choice == 1:
            view_all_products(inventory)
        
        elif choice == 2:
            add_product(inventory, transactions)
        
        elif choice == 3:
            update_stock(inventory, transactions)
        
        elif choice == 4:
            update_product_details(inventory)
        
        elif choice == 5:
            remove_product(inventory)
        
        elif choice == 6:
            search_products(inventory)
        
        elif choice == 7:
            view_low_stock(inventory)
        
        elif choice == 8:
            generate_category_report(inventory)
        
        elif choice == 9:
            view_transaction_log(transactions)
        
        elif choice == 10:
            handle_export_menu(inventory)
        
        elif choice == 11:
            # Save data before exiting
            print("\nSaving data...")
            save_inventory(inventory)
            save_transactions(transactions)
            print("\nThank you for using Murphy's General Store Inventory System!")
            print("Goodbye!")
            break

# =============================================================================
# FUNCTION 19 - A3 EXPORT SUBMENU (Copy as-is)
# =============================================================================

def handle_export_menu(inventory):
    """
    Display export submenu and handle export operations.
    
    NEW FOR A3 - Provides submenu for exporting reports in different formats.
    
    Parameters:
        inventory (dict): The inventory dictionary to export
    """
    from datetime import datetime
    
    print("\n--- Export Reports ---")
    print("1. Export inventory to CSV")
    print("2. Export low stock report to CSV")
    print("3. Generate formatted text report")
    print("4. Export all reports")
    print("5. Cancel")
    
    choice = get_valid_int("\nEnter your choice (1-5): ", min_value=1)
    
    while choice < 1 or choice > 5:
        print("Error: Please enter a number between 1 and 5")
        choice = get_valid_int("Enter your choice (1-5): ", min_value=1)
    
    if choice == 1:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"inventory_{timestamp}.csv"
        export_inventory_to_csv(inventory, filename)
        print(f"\nInventory exported to {filename}")
    
    elif choice == 2:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"low_stock_{timestamp}.csv"
        export_low_stock_to_csv(inventory, filename)
        print(f"\nLow stock report exported to {filename}")
    
    elif choice == 3:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"inventory_report_{timestamp}.txt"
        generate_text_report(inventory, filename)
        print(f"\nReport saved to {filename}")
    
    elif choice == 4:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        export_inventory_to_csv(inventory, f"inventory_{timestamp}.csv")
        export_low_stock_to_csv(inventory, f"low_stock_{timestamp}.csv")
        generate_text_report(inventory, f"inventory_report_{timestamp}.txt")
        print(f"\nInventory exported to inventory_{timestamp}.csv")
        print(f"Low stock report exported to low_stock_{timestamp}.csv")
        print(f"Report saved to inventory_report_{timestamp}.txt")
        print("\nAll reports exported successfully!")
    
    elif choice == 5:
        print("\nExport cancelled.")

if __name__ == "__main__":
    main()
