from stats import count_words, count_chars, sort_dict
import sys

def get_book_test(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_book = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    file_contents = get_book_test(path_to_book)
    num_words = count_words(file_contents)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    dict_chars = count_chars(file_contents)
    sorted_dict_list = sort_dict(dict_chars)
    print("--------- Character Count -------")
    for i in range(0, len(sorted_dict_list)):
        print(f"{sorted_dict_list[i]["char"]}: {sorted_dict_list[i]["num"]}")
    
    print("============= END ===============")

main()