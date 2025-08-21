# Nigerialn currency converter
amount = float(input("enter amount in naira: "))
exchange_rate_dollars = float(input("enter exchange rate to US DOllars: "))
exchange_rate_pounds =float(input("enter exchange rate to British pounds: ")) 

#conversion of currency from naira to dollas and pounds
amount_in_dollar = amount / exchange_rate_dollars
amount_in_pounds = amount / exchange_rate_pounds

print("Currency\t\t\tSymbol\tAmount")
print("----------------------------------------------------")
print(f"Amount in Naira\t\t\t₦\t{amount:,.2f}")
print(f"Amount in Dollar\t\t$\t{amount_in_dollar:,.2f}")
print(f"Amount in pounds\t\t£\t{amount_in_pounds:,.2f}")

