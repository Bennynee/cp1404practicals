import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.00
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILE_NAME = "stock_price.txt"

number_of_days = 0
price = INITIAL_PRICE

out_file = open(FILE_NAME, 'w')
print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    number_of_days += 1
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

out_file.close()