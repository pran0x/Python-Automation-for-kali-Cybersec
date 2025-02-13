
"""
        The function generates a custom wordlist based on input keywords with various permutations including
        case variations, number suffixes, special characters, and leet substitutions.
        
        :param keywords: The `keywords` parameter in the script refers to the base words or phrases that you
        want to use as a starting point for generating the custom wordlist. These keywords will be
        manipulated and combined with various permutations to create a list of potential passwords or
        phrases for testing or other purposes
        :param min_length: The `min_length` parameter in the `generate_wordlist` function specifies the
        minimum length that a generated word in the wordlist should have. Words shorter than this length
        will be excluded from the final wordlist, defaults to 4 (optional)
        :param max_length: The `max_length` parameter in the `generate_wordlist` function specifies the
        maximum length that a generated word can have. Words longer than this specified length will be
        filtered out from the final wordlist, defaults to 12 (optional)
        :param add_numbers: The `add_numbers` parameter in the `generate_wordlist` function determines
        whether number suffixes should be added to the base keywords to create variations. If set to `True`,
        number suffixes ranging from 0 to 99 and common years from 1950 to 2023 will be appended, defaults
        to True (optional)
        :param add_special_chars: The `add_special_chars` parameter in the `generate_wordlist` function
        determines whether special characters like '!', '@', '#', '$', '%', '&', '*' will be added to the
        generated wordlist. If `add_special_chars` is set to `True`, special characters will be appended to,
        defaults to True (optional)
        :param case_variations: The `case_variations` parameter in the `generate_wordlist` function controls
        whether variations of the base keywords with different cases (upper, lower, title) should be
        included in the wordlist. When `case_variations` is set to `True`, the function will add uppercase,
        lowercase,, defaults to True (optional)
        :param leet_substitutions: The `leet_substitutions` parameter in the `generate_wordlist` function
        controls whether leet (or 1337) substitutions are applied to the generated wordlist. Leet
        substitutions involve replacing letters with visually similar characters or numbers to create
        variations of the original words. For example, replacing 'a, defaults to True (optional)
        :return: The code defines a function `generate_wordlist` that takes base keywords and generates a
        custom wordlist with various permutations based on the provided options such as adding numbers,
        special characters, case variations, and l33t substitutions. The function returns a sorted list of
        words that meet the specified length criteria.
        """

import itertools
import argparse

def generate_wordlist(keywords, min_length=4, max_length=12, add_numbers=True, add_special_chars=True, case_variations=True, leet_substitutions=True):
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

    # Apply l33t substitutions
    if leet_substitutions:
        leet_map = {
            'a': ['4', '@'],
            'e': ['3'],
            'i': ['1', '!'],
            'o': ['0'],
            's': ['5', '$'],
            't': ['7']
        }
        new_words = set()
        for word in wordlist:
            leet_variations = set([word])
            for char, subs in leet_map.items():
                temp_variations = set()
                for variation in leet_variations:
                    for sub in subs:
                        temp_variations.add(variation.replace(char, sub))
                leet_variations.update(temp_variations)
            new_words.update(leet_variations)
        wordlist.update(new_words)

    # Filter by length
    filtered = [w for w in wordlist if min_length <= len(w) <= max_length]

    return sorted(filtered)

def save_wordlist(wordlist, filename="I33T.txt"):
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(f"{word}\n")
    print(f"Wordlist saved to {filename} ({len(wordlist)} entries)")

if __name__ == "__main__":
    print("-k : Keywords\n-o : Output\n")
    print("Example: python I33T_subtituition.py -k password -o I33T.txt\n")
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
        case_variations=True,
        leet_substitutions=True
    )

    # Save results
    save_wordlist(custom_list, args.output)