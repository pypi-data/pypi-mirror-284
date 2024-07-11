def calculate_initial_deposit(property_cost, down_payment, annual_loan_rate, loan_term_years, deposit_annual_rate,
                              desired_repayment_years):
    # Calculate the loan amount
    loan_amount = property_cost - down_payment

    # Convert annual rates to monthly rates
    monthly_loan_rate = annual_loan_rate / 12
    monthly_deposit_rate = deposit_annual_rate / 12

    # Number of loan months and desired repayment period
    loan_term_months = loan_term_years * 12
    desired_repayment_months = desired_repayment_years * 12

    # Annuity payment
    monthly_payment = loan_amount * (monthly_loan_rate * (1 + monthly_loan_rate) ** loan_term_months) / (
                (1 + monthly_loan_rate) ** loan_term_months - 1)

    # Modeling required deposit amount for early repayment
    remaining_balance = loan_amount
    deposit_balance = 0
    for month in range(desired_repayment_months):
        # Monthly interest accrual on deposit
        deposit_balance += deposit_balance * monthly_deposit_rate

        # Calculate remaining mortgage balance
        remaining_balance -= (monthly_payment - remaining_balance * monthly_loan_rate)

    # Calculate the required initial deposit amount
    initial_deposit = remaining_balance / ((1 + monthly_deposit_rate) ** desired_repayment_months)
    return initial_deposit


# Property cost
property_cost = 11100000
# Down payment
down_payment = 2231000
# Mortgage interest rate
annual_loan_rate = 0.05
# Loan term in years
loan_term_years = 30
# Deposit interest rate
deposit_annual_rate = 0.15
# Desired mortgage repayment period in years
desired_repayment_years = 10

initial_deposit_needed = calculate_initial_deposit(property_cost, down_payment, annual_loan_rate, loan_term_years,
                                                   deposit_annual_rate, desired_repayment_years)
print(f"Required deposit amount: {initial_deposit_needed:,.0f} RUB".replace(',', ' ') + f" to repay in {desired_repayment_years} years")
