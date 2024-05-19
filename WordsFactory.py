import string

def generate_wordlist():
    # Ask user for input
    base_words = input("What words do you want to include in the words list? (comma separated) ").split(',')
    base_words = [word.strip() for word in base_words]
    numbers_to_merge = input("What numbers do you want to merge with these words? (comma separated) ").split(',')
    numbers_to_merge = [num.strip() for num in numbers_to_merge]
    special_chars_to_merge = input("What special characters do you want to merge with these words? (comma separated) ").split(',')
    special_chars_to_merge = [char.strip() for char in special_chars_to_merge]

    # Generate word list
    words = set()
    for word in base_words:
        words.add(word)
        for num in numbers_to_merge:
            words.add(word + num)
            words.add(num + word)
        for char in special_chars_to_merge:
            words.add(word + char)
            words.add(char + word)

    # Write words to file
    with open('wordlist.txt', 'w') as f:
        for word in words:
            f.write(word + '\n')

    print("Generated word list and saved to wordlist.txt")

generate_wordlist()
