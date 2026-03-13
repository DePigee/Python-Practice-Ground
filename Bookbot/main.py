from stats import word_count

def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    num_words = word_count(text)
    print(f"Found {num_words} total words")

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

main()


