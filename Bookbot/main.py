def main():
    path_to_book = "books/frankenstein.txt"
    text = get_book_text(path_to_book)
    print(text)

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

main()


