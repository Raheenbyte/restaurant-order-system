menu={
    'Pizza':100,
    'Pasta':120,
    'Burger':70,
    "Tea":60,
}
print("welcome to RF restuant")
print(" pizza: Rs100\n pasta: Rs120\n burger:Rs70\n tea: Rs:60\n")
item_1=input("what you want to order?").title()
total_order=0
if item_1 in menu:
    total_order+=menu[item_1]
    print(f"Your order {item_1} has been done")
else:
    print(f"this item {item_1} is not avalable")
another_order=input("Do you want to add anything else (yes/no)?").title()
if another_order=='Yes':
    item_2=input("Enter your another order").title()
    if item_2 in menu:
        total_order+=menu[item_2]
        print("your order has been done")
    else:
        print(f"ordered {item_2} is not available yet")
else:
    print(f"The total amount you have to pay is Rs{total_order}")
print(f"total amount to pay Rs{total_order}")



