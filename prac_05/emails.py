"""
Emails exercise
Estimate: 10 minutes
Actual: 17 minutes
"""
email_to_name = {}
email = input("Email: ").strip()

while email != "":
    name_part = email.split('@')[0]
    name_parts = name_part.split('.')
    name = ' '.join(name_parts).title()
    confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
    if confirmation != "" and confirmation != "y":
        name = input("Name: ").strip().title()

    email_to_name[email] = name
    email = input("Email: ").strip()

for email, name in email_to_name.items():
    print(f"{name} ({email})")

