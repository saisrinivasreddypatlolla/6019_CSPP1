'''# Functions | Assignment-1 - Paying Debt off in a Year

# Write a program to calculate the credit card balance after one year
if a person only pays the minimum monthly payment required by the
# credit card company each month.
'''

def paying_debt_off_in_a_year(balance, annual_interest_rate, monthly_payment_rate):
    ''' input : 42 0.2 0.04
    output: 31.38'''
    previous_balance = balance
    for _ in range(12):
        monthly_intrest = (annual_interest_rate/12.0)
        minimum_monthly_payment = (monthly_payment_rate * previous_balance)
        monthly_unpaid_balance = previous_balance - minimum_monthly_payment
        updated_balance_each_month = monthly_unpaid_balance+(monthly_intrest*monthly_unpaid_balance)
        previous_balance = updated_balance_each_month
    return round(updated_balance_each_month, 2)
def main():
    '''this program is used to print the remaining balance of credit card after one year'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance:", paying_debt_off_in_a_year(data[0], data[1], data[2]))

if __name__ == "__main__":
    main()
