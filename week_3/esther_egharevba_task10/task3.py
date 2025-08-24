#Electricity Bill Formatter
try:
    #collecting cusomer's details
    customer_full_name = input("Enter Customer's full name: ")
    units_consumed = int(input("Enter units consumed: "))
    cost_per_unit = float(input("Enter cost per unit: "))

    #total bills
    total_bills = units_consumed * cost_per_unit

    # printing out Electricity Receipt
    print(f"Customer's full Name:\t{customer_full_name}\nunits consumed:\t\t{units_consumed}KWh\nTotal bills:\t\t#{total_bills}")
except ValueError as e:
    print("Error:", e)