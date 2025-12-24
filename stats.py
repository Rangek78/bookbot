def count_words(text):
    return len(text.split())

def count_chars(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_dict(unsorted_dict):
    dict_list = []
    for key in unsorted_dict:
        if key.isalpha():
            dict_list.append({"char": key, "num": unsorted_dict[key]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
