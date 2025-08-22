# simulated  ussed menu interaction
balance = 500
print("Welcome to Mobile banking!")
# user_code = int(input("dial *121#: "))
user_code = ""
while user_code != "*121#":
    user_code = input("dial *121#:\nenter ussed code: ")
    
# printing menu
while True:
    print("menu")
    print("1. Check  Balance\n2. Buy Airtime\n3. Buy Data\n4. Electricity Bill\n5. exit")

# options 1 for users to enter
    choose_option = input("choose an option: ")
    if choose_option == "1":
        print("Check Balance")
        print(balance)
        break
    elif choose_option == "2":
        print("Buy Airtime")
        amount = int(input("Enter amount: "))
        user_number = input("Enter phone number:")
        if len(user_number) == 11 and user_number.isdigit():
            if amount <= balance:
                network = input("Enter your mobile network:\n1.GLO\n2.MTN\n3AIRTEL").lower()
                # print("TRANSACTION SUCCESSFUL")
                balance -= amount
                print("TRANSACTION SUCCESSFUL")
                break
            else:
                print("Insufficient Fund")  
                break
        else:
            print(f"{user_number} is not a number")
    elif choose_option == "3":
        print("Buy Data")
        available_data_amount = int(input("1. 1GB #250\n2.4.5GB   #1000\n3.7GB   #5000 \n4.11GB  #2.500: "))
        user_number1 = input("Enter phone number:").isdigit
        network = input("Enter your mobile network:\n1.GLO\n2.MTN\n3.AIRTEL").lower
        if user_number1 == user_number1 or len(11):
        
            if available_data_amount <= balance:
             available_data_amount -= balance
            print("TRANSACTION SUCCESSFUL")
        else:
            print("INSUFFICIENT FUND") 
        break
    elif choose_option == "4":
        print("Electricity Bill")
        bills = int(input("Enter your meter number\n Enter amount: "))
        balance -= bills
        break
    elif choose_option == "5":
        print("EXIT")
        break
    else:
        print("invalide Choice")