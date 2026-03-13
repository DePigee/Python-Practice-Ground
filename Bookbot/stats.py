def word_count(book_contents):
    split_words = book_contents.split()
    return len(split_words)

def count_characters(text):
    word_count_dict = {}
        
    lower_cased_chars = text.lower()
    for char in lower_cased_chars:
        if(char in word_count_dict):
            word_count_dict[char] += 1
        else:
            word_count_dict[char] = 1
    return word_count_dict
