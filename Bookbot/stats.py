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

def sort_on(dict):
    return dict["num"]

def sorted_list(dict):
    sorted_list = []

    for d in dict:
        sorted_list.append({"char" : d, "num": dict[d]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list    


    

   