import math

user_question = input('''
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' from the menu above to proceed: ''').lower().upper().capitalize()


if user_question == "investment".lower().upper().capitalize():
    investment_amount = float(input("Please insert the investment amount being deposited: "))
    investment_rate = float(input("Please insert the investment interest rate percentage: "))
    investment_rate = investment_rate/100
    investment_year = float(input("Please insert the investment amount of years: "))
    interest_type_sc = input("Please advise if you would like to calculate simple or compund interest: ").lower().upper().capitalize()
    
    
    if interest_type_sc == "simple".lower().upper().capitalize():
        total_price = round(investment_amount * (1 + investment_rate*investment_year),2)
        print(f"The total collected over simple interest '{investment_year} years' would be 'R {total_price}'")


    else: 
        interest_type_sc == "compound".lower().upper().capitalize()
        total_price = round(investment_amount * math.pow(1 + investment_rate,investment_year),2)
        print(f"The total collected over compound interest '{investment_year} years' would be 'R {total_price}'")


elif user_question == "bond".lower().upper().capitalize():
    bond_amount= float(input("Can you please insert a bond amount: "))
    bond_rate = float(input("Can you please insert the interest rate: "))
    bond_time = float(input("Please insert how many months you would like to calculate for :"))
    bond_rate = bond_rate/100
    bond_rate = bond_rate/12

    total_payment = round((bond_rate * bond_amount)/(1 - (1 + bond_rate)**(-bond_time)),2)
    print(f"The total monthly repayment for the bond is :'R {total_payment}'.")


else:
   print("Please restart the program invalid entry !!")