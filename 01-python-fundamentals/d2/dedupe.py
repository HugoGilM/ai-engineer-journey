duplicate_numbers = [3, 1, 3, 2, 1, 5]
deduped_numbers = list(
    dict.fromkeys(duplicate_numbers)
)  # Using dict.fromkeys to remove duplicates
print(deduped_numbers)  # Output: [1, 2, 3, 5] (order may vary)
