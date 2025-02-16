try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")

"""
When will a ValueError occur?
When the input is not an integer

When will a ZeroDivisionError occur?
When the denominator is 0


Could you change the code to avoid the possibility of a ZeroDivisionError?
I could check the value of the denominator and print out a statement 
"""