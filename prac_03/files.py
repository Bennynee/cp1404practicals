name = input("Enter your name: ")

file = open("name.txt", "w")
file.write(name)
file.close()

file = open("name.txt", "r")
name = file.read().strip()
file.close()

print(f"Hi {name}!")

with open("numbers.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())

result = first_number + second_number
print(result)

total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line)

print(total)




