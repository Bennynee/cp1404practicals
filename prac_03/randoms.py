import random


print(random.randint(5, 20))
print(random.randrange(3, 10, 2))
print(random.uniform(2.5, 5.5))

# The largest number in line 1 is 20, the smallest is 5

# The smallest number is 3, the largest is 9, it can not produce a 4 because
# the step of 2 skip all the even numbers, including 4

# The smallest number is 2.5, the largest number is 5.5

print(random.randint(1, 100))