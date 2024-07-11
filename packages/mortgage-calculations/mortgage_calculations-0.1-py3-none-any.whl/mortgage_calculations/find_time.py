def calculate_repayment_period(property_cost, down_payment, annual_loan_rate, loan_term_years, initial_deposit,
                               deposit_annual_rate):
    # Calculate the loan amount
    loan_amount = property_cost - down_payment

    # Convert annual rates to monthly rates
    monthly_loan_rate = annual_loan_rate / 12
    monthly_deposit_rate = deposit_annual_rate / 12

    # Number of loan months
    loan_term_months = loan_term_years * 12

    # Annuity payment
    monthly_payment = loan_amount * (monthly_loan_rate * (1 + monthly_loan_rate) ** loan_term_months) / (
                (1 + monthly_loan_rate) ** loan_term_months - 1)

    # Modeling monthly deposit growth and mortgage repayment
    remaining_balance = loan_amount
    deposit_balance = initial_deposit
    month = 0

    while remaining_balance > 0 and deposit_balance < remaining_balance:
        # Monthly interest accrual on deposit
        deposit_balance += deposit_balance * monthly_deposit_rate

        # Calculate remaining mortgage balance
        remaining_balance -= (monthly_payment - remaining_balance * monthly_loan_rate)

        month += 1

    years_to_repay = month / 12
    return years_to_repay


# Property cost
property_cost = 11100000
# Down payment
down_payment = 2231000
# Mortgage interest rate
annual_loan_rate = 0.05
# Loan term in years
loan_term_years = 30
# Initial deposit amount
initial_deposit = 1000000
# Deposit interest rate
deposit_annual_rate = 0.11

repayment_period = calculate_repayment_period(property_cost, down_payment, annual_loan_rate, loan_term_years,
                                              initial_deposit, deposit_annual_rate)
print(f"Mortgage repayment period: {repayment_period:.2f} years")
