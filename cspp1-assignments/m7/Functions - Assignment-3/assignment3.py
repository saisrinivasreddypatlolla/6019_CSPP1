'''# Functions - Assignment-3 - Using Bisection Search to Make the Program Faster

'''



def payingDebtOffInAYear(balance, annualInterestRate):
    '''input 320000 0.2
    output: 29157.09'''
    previous_balance = balance
    monthly_interest_rate = annualInterestRate/12
    monthly_payment_lowerbound = previous_balance/12
    monthly_payment_upperbound = (previous_balance*(1+monthly_interest_rate)**12)/12.0
    epsilon = 0.03
    while abs(balance)> epsilon:
        monthly_payment = (monthly_payment_lowerbound+monthly_payment_upperbound)/2
        balance = previous_balance
        for _ in range(12):
            Monthly_unpaid_balance = (balance) - (monthly_payment)
            balance = (Monthly_unpaid_balance) + (monthly_interest_rate * Monthly_unpaid_balance)
        if balance > epsilon:
            monthly_payment_lowerbound = monthly_payment
        elif balance < -epsilon:
            monthly_payment_upperbound = monthly_payment
    return str(round(monthly_payment,2))

def main():
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment:",payingDebtOffInAYear(data[0], data[1]))
    
if __name__ == "__main__":
    main()
