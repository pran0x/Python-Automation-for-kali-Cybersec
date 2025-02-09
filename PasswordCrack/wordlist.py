import itertools
import argparse

def generate_wordlist(keywords, min_length=4, max_length=12, add_numbers=True, add_special_chars=True, case_variations=True):
    """
    Generate a custom wordlist from base keywords with various permutations.
    """
    wordlist = set()

    # Add base keywords
    for word in keywords:
        wordlist.add(word.strip())

    # Case variations (upper/lower/title)
    if case_variations:
        new_words = set()
        for word in wordlist:
            new_words.add(word.upper())
            new_words.add(word.lower())
            new_words.add(word.title())
        wordlist.update(new_words)

    # Add number suffixes (e.g., "password2023")
    if add_numbers:
        numbers = [str(i) for i in range(0, 100)]  # 0-99
        years = [str(i) for i in range(1950, 2024)]  # Common year formats
        suffixes = numbers + years
        
        new_words = set()
        for word in wordlist:
            for suffix in suffixes:
                new_words.add(f"{word}{suffix}")
        wordlist.update(new_words)

    # Add special characters
    if add_special_chars:
        special_chars = ['!', '@', '#', '$', '%', '&', '*']
        new_words = set()
        for word in wordlist:
            for char in special_chars:
                new_words.add(f"{word}{char}")
                new_words.add(f"{char}{word}")
        wordlist.update(new_words)

    # Filter by length
    filtered = [w for w in wordlist if min_length <= len(w) <= max_length]

    return sorted(filtered)

def save_wordlist(wordlist, filename="custom_wordlist.txt"):
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(f"{word}\n")
    print(f"Wordlist saved to {filename} ({len(wordlist)} entries)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate custom wordlists")
    parser.add_argument("-k", "--keywords", nargs="+", required=True,
                        help="Base keywords (e.g., names, locations)")
    parser.add_argument("-o", "--output", default="custom_wordlist.txt",
                        help="Output filename")
    args = parser.parse_args()

    # Generate wordlist
    custom_list = generate_wordlist(
        keywords=args.keywords,
        min_length=6,
        max_length=16,
        add_numbers=True,
        add_special_chars=True,
        case_variations=True
    )

    # Save results
    save_wordlist(custom_list, args.output)