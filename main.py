import sys
from stats import get_book_text, get_word_count, list_char_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    
    book_contents = get_book_text(file_path)
    word_count = get_word_count(book_contents)
    char_count = list_char_count(book_contents)
    print_list(book_contents, word_count, char_count)

def print_list(file_path, word_count, char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in char_count:
        if not char["char"].isalpha():
            continue
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")

main()