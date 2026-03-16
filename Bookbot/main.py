from stats import word_count, count_characters, sorted_list

def main():
    path_to_book = "books/frankenstein.txt"
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
    print(f"{num_words} Found")
    print("--------- Character Count -------")

    for item in sorted_dict:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()


