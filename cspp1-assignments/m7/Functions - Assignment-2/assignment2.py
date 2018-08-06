'''# Assignment-2 - Paying Debt off in a Year

# Now write a program that calculates the minimum fixed monthly payment needed in order
pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not change each month,
but instead is a constant amount that will be
# paid each month.

# In this problem, we will not be dealing with a minimum monthly payment rate.

# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal
'''

def paying_debt_offin_a_year(balance, annual_interest_rate):
    '''input 3329 0.2
    output 310'''
    previous_balance = balance
    assume_val = 10
    if balance <= 0:
        return 0
    while balance > 0:
        balance = previous_balance
        monthly_interest = annual_interest_rate/12
        for _ in range(12):
            monthly_unpaid = balance - assume_val
            updated_balance_eachmonth = monthly_unpaid + (monthly_interest*monthly_unpaid)
            balance = updated_balance_eachmonth
        assume_val += 10
    assume_val = assume_val-10
    return round(assume_val, 2)


def main():
    '''this program is used to print the fixed amount of the credit balance'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:", str(paying_debt_offin_a_year(data[0], data[1])))

if __name__ == "__main__":
    main()
