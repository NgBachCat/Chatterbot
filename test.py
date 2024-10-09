def calculate_electricity_bill(units):
    if units <= 100:
        bill = 0
    elif units <= 200:
        bill = (units - 100) * 5
    else:
        bill = (100 * 5) + (units - 200) * 10

    return bill

# Accept number of units from user
units = int(input("Enter the number of units: "))
bill_amount = calculate_electricity_bill(units)
print(f"Total bill amount is Rs {bill_amount}")