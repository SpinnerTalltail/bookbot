import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
from stats import num_words
from stats import count_chars
from stats import dict_list

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + sys.argv[1] + "...")
    print("----------- Word Count ----------")
    print(f"Found {num_words()} total words")
    print("--------- Character Count -------")
    for item in dict_list():
        ch = item["char"]
        num = item["num"]
        print(f"{ch}: {num}")
    print("============= END ===============")

main()


