# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

RestockThresh = 30
DiscountThresh = 100

for item in inventory:
    print(f'{item}: {inventory[item]}')
    if inventory[item][0] < RestockThresh:
        print(f'{item} need restocking.')
    elif inventory[item][0] > RestockThresh and inventory[item][0] < DiscountThresh:
        print(f'{item} should be sold at the regular price of {inventory[item][1]}.')
    elif inventory[item][0] > DiscountThresh:
        print(f'{item} should be sold at the discounted price of {inventory[item][2]:.2f}.')

