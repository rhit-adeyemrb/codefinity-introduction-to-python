# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

# code
print('Processing Started')

for item in inventory:
    # print (range(len(inventory)))
    print(f'Processing for {item}')
    while inventory[item][0] < inventory[item][1]: #chcking satus of stock
        print(f'{item}: {inventory.get(item)}')
        if inventory[item][0] > discount_threshold:
            inventory[item][3] = True #changing sale status 
        else:
            None
        inventory[item][0]+= inventory[item][2] # restocking
    print(f'{item} Now: {inventory.get(item)}') # printing updated inventory
print('Processing completed!')

                