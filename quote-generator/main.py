import random

# Each quote is a (quote, author) tuple.
QUOTES = [
    ("The only way to do great work is to love what you do.", "Steve Jobs"),
    ("Whether you think you can or you think you can't, you're right.", "Henry Ford"),
    ("It does not matter how slowly you go as long as you do not stop.", "Confucius"),
    ("Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill"),
    ("Believe you can and you're halfway there.", "Theodore Roosevelt"),
    ("The best time to plant a tree was 20 years ago. The second best time is now.", "Chinese Proverb"),
    ("Everything you've ever wanted is on the other side of fear.", "George Addair"),
    ("Hardships often prepare ordinary people for an extraordinary destiny.", "C.S. Lewis"),
    ("The only limit to our realization of tomorrow is our doubts of today.", "Franklin D. Roosevelt"),
    ("Do what you can, with what you have, where you are.", "Theodore Roosevelt"),
    ("Act as if what you do makes a difference. It does.", "William James"),
    ("Quality is not an act, it is a habit.", "Aristotle"),
]


def random_quote():
    """Return a single (quote, author) tuple chosen at random."""
    return random.choice(QUOTES)


def main():
    quote, author = random_quote()
    print(f'"{quote}" — {author}')


if __name__ == "__main__":
    main()
