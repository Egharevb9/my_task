# simulated USSD menu interaction
print("Welcome to moblie banking!")
dial = input("dial *121#: ")
print("1. Check Balance\n2. Buy Airtime\n3.Buy Data ")
option = int(input("choose an option between 1, 2 and 3: "))
print(f"you selected option {option}")
amount =int(input("please enter your amount: "))
print("transaction successful")
