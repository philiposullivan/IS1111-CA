# inventory_v1.py
# Name: [Your Name]
# Student ID: [Your Student ID]
# Date: [Date]
# Description: Product Inventory Management System using a 2D List
#              for Murphy's General Store (Assignment 1)

# =============================================================================
# ASSIGNMENT 1: List-Based Inventory (Version 1.0)
# =============================================================================
#
# For complete instructions, step-by-step guidance, sample outputs,
# and implementation checklists, see A1_INSTRUCTIONS.txt
#
# Quick Reference:
# ----------------
# - Use ONE main list called 'inventory' containing sub-lists.
# - Each sub-list: [name, category, price, quantity, min_stock]
# - Use the CONSTANTS provided below to access data safely.
#
# =============================================================================

# --- CONSTANTS ---
# Use these variables to access data in your sub-lists.
# This makes your code readable. "product[IDX_PRICE]" is clearer than "product[2]"

# Assign the corresponding index values to the variables below
IDX_NAME = 
IDX_CATEGORY = 
IDX_PRICE = 
IDX_QTY = 
IDX_MIN = 

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_valid_float(prompt, min_value=0.0):
    """
    Repeatedly asks user for input until a valid float is entered.
    Returns the valid float.
    """
    # Write your code here (use while, try/except and a conditional)
    # Note that in some cases the default min_value may not apply
    # (e.g., price shouldn't be zero).
    pass # Remove this pass when you start coding

def get_valid_int(prompt, min_value=0):
    """
    Repeatedly asks user for input until a valid integer is entered.
    Returns the valid integer.
    """
    # Write your code here (use while, try/except and a conditional)
    # Note that in some cases the default min_value may not apply
    # (e.g., price shouldn't be zero).
    pass # Remove this pass when you start coding

# You may add other helper functions as needed 

# =============================================================================
# CORE FUNCTIONS
# =============================================================================
# Write your functions below.
# Refer to the sample outputs in the instructions for formatting guidance.

# Function to display the main menu and get user choice
# - Print formatted menu
# - Use validation function to ensure choice is between 1 and 7
# - Keep asking until valid range

# Function to view all products in the inventory in a formatted table
# - Check if inventory is empty
# - Print table header
# - Print each product using index constants

# Function to add a new product to the inventory
# - Get product name and check for duplicates (case-insensitive)
# - Loop through inventory to check if product already exists
# - Get remaining product details with validation
# - Create new product sub-list and append to inventory

# Function to update stock quantity of a product
# - Get product name to update
# - Find the product in inventory
# - Check if product exists
# - Ask whether it's a sale or delivery
# - Validate transaction type (loop until valid option entered by user)
# - Get quantity
# - Process sale (update stock)
# - Process delivery (update stock)

# Function to remove a product from the inventory
# - Get product name to remove
# - Find the product's index in inventory
# - Check if product exists
# - Confirm removal (ask if user is sure they want to remove it)
# - Use a list method to remove the product sub-list

# Function to view low stock products in formatted table
# - Find products with low stock
# - If no product needs restocking, print message
# - Print table header
# - Display each low stock product with amount to order

# Function to calculate total inventory value
# - Sum up (price * quantity) for each product


# =============================================================================
# MAIN PROGRAMME
# =============================================================================

if __name__ == "__main__":

    # You may write the following code directly here, or
    # define a main() function above and call it from here
    
    # 1. Initialise the inventory list
    # Structure: [name, category, price, quantity, min_stock]


    # 2. Display a welcome message
    

    # 3. Your main menu loop goes here
    # - Display menu
    # - Get user choice
    # - Call appropriate function based on choice
    # - Repeat until user exits
    # - Display results or error messages

    # Example structure:
    # while True:
    #     choice = display_menu()  # Call your menu function
    #     if choice == 1:
    #         # Call function for option 1
    #     elif choice == 2:
    #         # Call function for option 2
    #     # ... etc

    # 4. Display a goodbye message when exiting

    pass  # Remove this and add your code here



# =============================================================================
# REFERENCES & AI STATEMENT
# =============================================================================
# References to any external sources used (following Canvas guidelines):
#
#
# AI Tool Usage:
# If AI tools were used, provide complete transparency including prompts,
# responses, and how you adapted them. Add working link to chat(s). 
# If not used, state: "No AI tools used."
#
#
# =============================================================================

# =============================================================================
# SELF-REFLECTION (2-3 sentences)
# =============================================================================
# Write about the most challenging aspect of this assignment 
# and what you learned from it:
#
#
#
# =============================================================================