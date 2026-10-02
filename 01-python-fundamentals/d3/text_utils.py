import string


def normalize(text: str) -> list[str]:
    """Lowercase the text, split it into words and strip surrounding punctuation."""
    words = [word.strip(string.punctuation) for word in text.lower().split()]
    return [word for word in words if word]  # Drop tokens that were only punctuation.


def count_words(words: list[str]) -> dict[str, int]:
    """Return a dictionary mapping each word to how many times it appears."""
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


def top_n(counts: dict[str, int], n: int = 10) -> list[tuple[str, int]]:
    """Return the n most frequent (word, count) pairs, ties broken alphabetically."""
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
