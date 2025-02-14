"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

MINIMUM_SALE = 0
LOW_SALES_DISCOUNT = 0.1
HIGH_SALES_DISCOUNT = 0.15
BONUS_LIMIT = 1000

sales = float(input("Enter sales: "))

while sales >= MINIMUM_SALE:
    if sales < BONUS_LIMIT:
        bonus = sales * LOW_SALES_DISCOUNT
    else:
        bonus = sales * HIGH_SALES_DISCOUNT
    print(f"The bonus is ${bonus}")
    sales = float(input("Enter sales: "))

print()