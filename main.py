from stats import get_num_words, count_characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = count_characters(text)
    print(f"{num_words} words found in the document")
    print(num_characters)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()