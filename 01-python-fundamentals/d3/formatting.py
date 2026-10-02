print(__name__)


def format_table(
    rows: list[tuple[str, int]], headers: tuple[str, str] = ("Word", "Count")
) -> str:
    """Return the rows as a text table: first column left-aligned, second right-aligned."""
    word_width = max([len(headers[0])] + [len(word) for word, _ in rows])
    count_width = max([len(headers[1])] + [len(str(count)) for _, count in rows])

    lines = [f"{headers[0]:<{word_width}}  {headers[1]:>{count_width}}"]
    lines.append("-" * (word_width + 2 + count_width))
    for word, count in rows:
        lines.append(f"{word:<{word_width}}  {count:>{count_width}}")
    return "\n".join(lines)
