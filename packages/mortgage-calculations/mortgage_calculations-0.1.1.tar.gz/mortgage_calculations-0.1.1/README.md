# Mortgage Calculator

This package provides functions to calculate the repayment period and the initial deposit needed to repay a mortgage within a desired period.

## Installation

```bash
pip install mortgage_calculations
```

## Usage

`from mortgage_calculations import calculate_repayment_period, calculate_initial_deposit`

# Example usage for repayment period calculation
```property_cost = 11100000
down_payment = 2231000
annual_loan_rate = 0.05
loan_term_years = 30
initial_deposit = 1000000
deposit_annual_rate = 0.11```

repayment_period = calculate_repayment_period(property_cost, down_payment, annual_loan_rate, loan_term_years,
                                              initial_deposit, deposit_annual_rate)
print(f"Mortgage repayment period: {repayment_period:.2f} years")

# Example usage for initial deposit calculation
desired_repayment_years = 10
initial_deposit_needed = calculate_initial_deposit(property_cost, down_payment, annual_loan_rate, loan_term_years,
                                                   deposit_annual_rate, desired_repayment_years)
print(f"Required deposit amount: {initial_deposit_needed:,.0f} RUB".replace(',', ' ') + f" to repay in {desired_repayment_years} years")
