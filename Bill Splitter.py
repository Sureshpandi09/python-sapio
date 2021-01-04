Total_cost=int(input("What was the bill?\n"))
persons=int(input("How many are sharing?\n"))
tip=input("Would you like to tip?(Yes/No)\n")
if tip=="Yes":
    tips = int(input("What % of bill would you like to tip?\n"))
    bill=(((Total_cost*tips)/100)+Total_cost)/persons
    print(f'Cost per person:{bill}')
else:
    bill=Total_cost/persons
    print(f'Cost per person:{bill}')
print("\nHave a nice day!!!")

