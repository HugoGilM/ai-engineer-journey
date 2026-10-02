# Exercise 1: stats(*numbers) -> (min, max, average)
def stats(*numbers: float) -> tuple[float, float, float] | None:
    if not numbers:
        return None
    return min(numbers), max(numbers), sum(numbers) / len(numbers)


# Passing arguments individually
print(stats(4, 8, 15))  # (4, 15, 9.0)

# Unpacking a list into positional arguments
my_list = [16, 23, 42]
print(stats(*my_list))  # (16, 42, 27.0)

# No arguments
print(stats())  # None


# Exercise 2: Fix the trap.

# Wrong: mutable default argument


def tag(word, tags=[]):
    tags.append(word)
    return tags


print(tag("python"))  # ['python']
print(
    tag("java")
)  # ['python', 'java'] - unexpected behavior due to mutable default argument
print(tag("c++"))  # ['python', 'java', 'c++'] - continues to accumulate


# Correct: use None as the default and create a new list inside the function
def tag_fixed(word, tags=None):
    if tags is None:
        tags = []
    tags.append(word)

    return tags


print(tag_fixed("python"))  # ['python']
print(tag_fixed("java"))  # ['java'] - now behaves as expected
print(tag_fixed("c++"))  # ['c++'] - no accumulation


# Exercise 3: *args y **kwargs


def build_url(base, **params):
    if not params:
        return base

    query_string = "&".join(f"{key}={value}" for key, value in params.items())
    return f"{base}?{query_string}"


print(build_url("https://api.x.com/search", q="python", page=2))
