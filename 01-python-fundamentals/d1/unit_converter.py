KM_TO_MILES = 0.621371
KG_TO_POUNDS = 2.20462

km = float(input("Enter distance in kilometers: "))
kg = float(input("Enter weight in kilograms: "))

rows = [
    ("Distance", km, "km", km * KM_TO_MILES, "mi"),
    ("Weight", kg, "kg", kg * KG_TO_POUNDS, "lb"),
]

print()
print(f"{'Measure':<10}{'From':>14}{'To':>14}")
print("-" * 38)
for label, value, unit, converted, new_unit in rows:
    print(f"{label:<10}{value:>11.2f} {unit}{converted:>11.2f} {new_unit}")
