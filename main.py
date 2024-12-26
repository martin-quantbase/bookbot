def print_report(report, total_words):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{total_words} words found in the document")
    print()
    sorted_list = sorted(report.items(), key=lambda x: x[1], reverse=True)
    for item in sorted_list:
        print(f"The '{item[0]}' character was found {item[1]} times")
    print(f"--- End report ---")
    return None


def count_character_usage(text):
    char_usage = {}
    for char in text.lower():
        if char.isalpha():
            if (char in char_usage):
                char_usage[char] += 1
            else:
                char_usage[char] = 1
    return char_usage


def count_words(text):
    return len(text.split())


def get_book_text():
    with open("./books/frankenstein.txt", 'r') as f:
        book_text = f.read()
    return book_text


def main():
    book = get_book_text()
    num_words = count_words(book)
    char_usage = count_character_usage(book)
    print_report(char_usage, num_words)


main()
