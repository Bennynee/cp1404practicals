DISCOUNT_RATE = 0.1
DISCOUNT_VALUE = 100
MINIMUM_ITEM = 0

total = 0
number_of_item = int(input("Enter number of items: "))

while number_of_item <= MINIMUM_ITEM:
    print("Invalid number of items!")
    number_of_item = int(input("Enter number of items: "))

for i in range(number_of_item):
    price = float(input("Price of item: "))
    total += price

if total > DISCOUNT_VALUE:
    total *= 1 + DISCOUNT_RATE

print(f"Total price for {number_of_item} items is ${total:,.2f}")