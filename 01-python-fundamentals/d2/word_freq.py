import string
from collections import Counter

multiline_text = """This is a multiline string.
It can span multiple lines. 
It is often used for documentation or long text blocks."""

print(multiline_text)

normalized_text = multiline_text.lower().split()

words = [word.strip(string.punctuation) for word in normalized_text]
total_words = len(words)

print(words)
print(f"Total words: {total_words}")


# Print the top 10 words in aligned columns, sorted by count (highest first),
# with ties broken alphabetically.
# Hint: use sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])).
# Each item is a (word, count) tuple, and sorting by the tuple (-count, word)
# means "count descending, then word ascending."

counts: dict[str, int] = {}  # Stores each word and its frequency.

for word in words:  # Process every word, including repeated ones.
    # get() returns 0 when word is missing; this assignment creates the key.
    counts[word] = counts.get(word, 0) + 1

print(counts)  # Print the dictionary of word counts.

top_10 = sorted(
    counts.items(),  # Produces (word, count) pairs.
    # kv[0] is the word; -kv[1] sorts higher counts first, then words alphabetically.
    key=lambda kv: (-kv[1], kv[0]),
)[:10]  # Keep the first 10 pairs after sorting.

print(f"{'Word':<15}{'Count':>5}")  # Print aligned column headings.
for word, count in top_10:  # Unpack each pair into its word and frequency.
    print(f"{word:<15}{count:>5}")  # Left-align word; right-align count.


# Stretch: Counter counts the words and most_common returns the 10 most frequent.
counter_counts = Counter(words)
counter_top_10 = counter_counts.most_common(10)

print(f"\nCounter: {counter_counts}")
print(f"\nCounter top 10: {counter_top_10}")


print("\nCounter top 10 (ties are not alphabetical):")
print(f"{'Word':<15}{'Count':>5}")
for word, count in counter_top_10:
    print(f"{word:<15}{count:>5}")
