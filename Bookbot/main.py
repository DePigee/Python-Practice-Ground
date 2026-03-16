from stats import word_count, count_characters, sorted_list
import sys



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]

    text = get_book_text(path_to_book)
    num_words = word_count(text)
    counted_characters = count_characters(text)

    sorted_dict = sorted_list(counted_characters) 

    print_report(path_to_book, num_words, sorted_dict)

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def print_report(path_to_book, num_words, sorted_dict):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_dict:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()


