IVA_RATE = 0.16
WIDTH = 32

items = [
    ("Coffee", 45.00),
    ("Croissant", 38.50),
    ("Orange juice", 52.00),
]


def money(amount):
    return f"${amount:,.2f}"


# f"[{'hi':>6}]"                # '[    hi]'        right-align in width 6 (C#: {x,6})
# f"[{'hi':<6}]"                # '[hi    ]'        left-align


def line(label, amount):
    print(f"{label:<20}{money(amount):>12}")


subtotal = sum(price for _, price in items)
iva = subtotal * IVA_RATE
total = subtotal + iva

print("=" * WIDTH)
print(f"{'RECEIPT':^{WIDTH}}")
print("=" * WIDTH)
for name, price in items:
    line(name, price)
print("-" * WIDTH)
line("Subtotal", subtotal)
line("IVA (16%)", iva)
print("=" * WIDTH)
line("TOTAL", total)
print("=" * WIDTH)
