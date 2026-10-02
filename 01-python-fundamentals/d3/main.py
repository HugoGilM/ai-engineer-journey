from formatting import format_table
from text_utils import count_words, normalize, top_n

TEXT = """This is a multiline string.
It can span multiple lines.
It is often used for documentation or long text blocks."""


def main() -> None:
    """Count the words in TEXT and print the most frequent ones as a table."""
    words = normalize(TEXT)
    counts = count_words(words)

    print(f"Total words: {len(words)}\n")

    print("Top 10 (default n):")
    print(format_table(top_n(counts)))

    print("\nTop 3 (keyword argument):")
    print(format_table(top_n(counts, n=3)))


if __name__ == "__main__":
    main()
