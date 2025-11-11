import sys

def get_book_text():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
    return file_contents

def num_words():
    return len(get_book_text().split())

def count_chars():
    char_dict = {}
    characters = get_book_text().lower()
    for char in characters:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def dict_list():
    char_dictionary = count_chars()
    new_list = [{"char": key, "num": value} for key, value in char_dictionary.items() if key.isalpha()]
    new_list.sort(key = lambda x: x["num"], reverse=True)
    return new_list

