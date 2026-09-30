persons = {"ana": "eng", "luis": "sales", "eva": "eng"}
grouped: dict[str, list[str]] = {}

for name, department in persons.items():
    if department not in grouped:
        grouped[department] = []
    grouped[department].append(name)

print(grouped)


# Exercise 3: Loops to comprehensions
numbers = range(1, 20)
squares = [n**2 for n in numbers if n % 2 == 0]
print(squares)

# dict mapping
words = ["api", "python", "dotnet", "go", "rust", "goes"]
word_lengths = {word: len(word) for word in words}
words_grouped: dict[int, list[str]] = {}


for word, length in word_lengths.items():
    if length > 3:
        if length not in words_grouped:
            words_grouped[length] = []
        words_grouped[length].append(word)

print(words_grouped)

# Same grouping with setdefault
words_grouped_compact: dict[int, list[str]] = {}

for word in words:
    length = len(word)
    if length > 3:
        words_grouped_compact.setdefault(length, []).append(word)

print(words_grouped_compact)


# first set

first_letters = {word[0] for word in words}
print(first_letters)  # {'a', 'p', 'd', 'g', 'r'}
