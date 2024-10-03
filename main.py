def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_frequency = count_char_frequency(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    
    sorted_dict_desc = dict(sorted(char_frequency.items(), key=lambda item: item[1], reverse=True))
    for char in sorted_dict_desc:
        if char.isalpha():
            print(f"The '{char}' character was found {sorted_dict_desc[char]} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_char_frequency(text):
    char_freq = {}
    text = text.lower()
    for char in text:
        char_freq[char] = char_freq.get(char, 0) + 1
    return char_freq


    
main()