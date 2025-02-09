import random


def main():
    score = float(input("Enter score: "))
    result = determine_score(score)
    print(f"Result: {result}")
    random_score = random.uniform(0, 100)
    random_result = determine_score(random_score)
    print(f"\nRandom score: {random_score:.2f}")
    print(f"Result: {random_result}")


def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    else:
        if score > 90:
            return "Excellent"
        elif score > 50:
            return "Passable"
        else:
            return "Bad"


main()