# creating an empty dictionary
store_items = {}

lists = ("clothes", "bag" ,"jweries", "shoes" ,"belt")
try:
    # Storing an item and it price provided by the users into store_item
    for item in lists:
        store_items[item] = float(input(f"Enter the price for {item}: "))
    print(store_items)

    # available items
    all_items = store_items.keys()
    print(all_items)

    updated_items = input("enter the item that you want to update").lower()
    print(store_items)
    if updated_items in store_items.keys():
        store_items[updated_items] = float(input("enter your price: "))
    else:
        print("invalide item")
    print(store_items)
except ValueError as e:
    print("Error:", e)
except KeyError:
    print("Invalid item (key not avialable)")
finally:
    print("Program closed") 