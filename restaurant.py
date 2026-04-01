menu = {
    'Pizza': 100,
    'Pasta': 120,
    'Burger': 70,
    'Tea': 60,
}

print("Welcome to RF Restaurant")
print(" Pizza: Rs100\n Pasta: Rs120\n Burger: Rs70\n Tea: Rs60\n")

total_order = 0
order_placed = False

item_1 = input("What do you want to order? ").title()

if item_1 in menu:
    total_order += menu[item_1]
    order_placed = True
    print(f"Your order '{item_1}' has been placed!")
else:
    print(f"Sorry, '{item_1}' is not available.")

another_order = input("Do you want to add anything else? (yes/no) ").title()

if another_order == 'Yes':
    item_2 = input("Enter your next order: ").title()
    if item_2 in menu:
        total_order += menu[item_2]
        order_placed = True
        print(f"Your order '{item_2}' has been placed!")
    else:
        print(f"Sorry, '{item_2}' is not available.")

# Only show total if at least one item was ordered
if order_placed:
    print(f"\nTotal amount to pay: Rs{total_order}")
else:
    print("No valid items were ordered.")


