total = float(input("Enter the total bill amount: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
number_people = int(input("Enter the number of people splitting the bill: "))
print(f"Person share: ${total * (1 + tip_percentage / 100) / number_people:.2f}")
