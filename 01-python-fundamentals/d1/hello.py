print(10 / 5)
print(-9 // 4)
print("5" * 3)
print(bool(""), bool(" "), bool(0.0))
print("abcdef"[1:-1])
print((0.1 + 0.2) == 0.3)


##############################

s = "  The Quick Brown Fox  "
print(
    s.strip().lower()
)  # Removes leading and trailing whitespace and converts to lowercase

print("-".join(s.strip().lower().split()))


print(s.strip()[::-1])
print(s.split()[-1])  # Splits the string into words and returns the last word

#################

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")
kelvin = celsius + 273.15
print(f"Temperature in Kelvin: {kelvin}")
