menu = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter name: ")
print(menu)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    if choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(menu)
    choice = input(">>> ").upper()

print("Finished.")