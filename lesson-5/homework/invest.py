def invest(amount, rate, years):
    for y in range(1,years+1):
        res=amount+rate*amount
        res=round(res,2)
        print(f"year {y}: ${res}")
        amount=res
principal_amount=int(input("Enter the principal amount: "))
annual_rate_of_return=float(input("Enter the annual rate of return in decimal: "))
number_of_years=int(input("Enter the number of years: "))
invest(principal_amount,annual_rate_of_return,number_of_years)