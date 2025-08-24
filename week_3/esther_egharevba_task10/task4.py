# school fees breakdown
try:
    school_name = input("enter school name: ")
    tuition_fee = float(input("Enter tuition fee: "))
    hostel_fee = float(input("Enter hostel fee: "))
    feeding_fee = float(input("Enter feeding fee: "))
    total = tuition_fee + hostel_fee +feeding_fee
    print(f"School Name:\t{school_name}\nTuition Fee:\t{tuition_fee}\nHostel fee:\t{hostel_fee}\nFeeding fee:\t{feeding_fee}\nTotal:\t\t{total}")
except ValueError as e:
    print("Error:", e)