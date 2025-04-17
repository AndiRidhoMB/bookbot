from stats import get_num_words, count_characters, sort_on_key
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = count_characters(text)
    sorted_num_characters = sort_on_key(num_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...\n")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words\n")
    print("--------- Character Count -------")
    for item in sorted_num_characters:
        # .isalpha used to only print alphabetical characters
        if item["char"].isalpha():
            print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()