"""my_toolkit.py — a small collection of utility functions.
 
Each function is implemented with explicit logic (no shortcut built-ins where
the exercise forbids them) and documented with a docstring.
"""
 
 
def calculate_average(numbers):
    """Return the arithmetic mean of a list of numbers.
 
    Returns 0 if the list is empty (avoids a division-by-zero error).
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
 
 
def find_max_and_min(numbers):
    """Return a tuple (max_value, min_value) for a list of numbers.
 
    Implemented with a manual loop instead of the built-in max()/min().
    Returns (None, None) for an empty list.
    """
    if not numbers:
        return (None, None)
 
    max_value = numbers[0]
    min_value = numbers[0]
    for n in numbers[1:]:
        if n > max_value:
            max_value = n
        if n < min_value:
            min_value = n
    return (max_value, min_value)
 
 
def count_occurrences(items, target):
    """Return the number of times target appears in items.
 
    Implemented with a manual loop instead of the built-in list.count().
    """
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count
 
 
def is_palindrome(text):
    """Return True if text reads the same forward and backward.
 
    Comparison is case-insensitive and ignores spaces.
    Examples: "racecar" -> True, "hello" -> False,
    "A man a plan a canal Panama" -> True.
    """
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
 
 
def create_report(title, scores):
    """Return a formatted multi-line report string for a list of scores.
 
    Uses calculate_average and find_max_and_min internally. Returns the
    report as a string (does not print it).
    """
    average = calculate_average(scores)
    max_value, min_value = find_max_and_min(scores)
 
    lines = [
        f"=== {title} ===",
        f"Number of scores: {len(scores)}",
        f"Average: {average:.2f}",
        f"Highest:  {max_value}",
        f"Lowest:   {min_value}",
    ]
    return "\n".join(lines)
 
 
if __name__ == "__main__":
    # Test each function
    test_scores = [85, 92, 78, 95, 88, 70, 93]
    print(f"Average: {calculate_average(test_scores)}")
    print(f"Max/Min: {find_max_and_min(test_scores)}")
    print(f"Count of 85: {count_occurrences(test_scores, 85)}")
    print(f"'racecar' palindrome: {is_palindrome('racecar')}")
    print(f"'hello' palindrome: {is_palindrome('hello')}")
    print()
    print(create_report("Class Scores", test_scores))