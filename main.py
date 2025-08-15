import sys
from stats import get_num_words
from stats import get_num_chars
from stats import sorted_list
from stats import get_book_text


def main(path_to_book):
    #path_to_book = "books/frankenstein.txt"
    word_number = get_num_words(get_book_text(path_to_book))
    char_dict = get_num_chars(get_book_text(path_to_book))
    get_num_chars(get_book_text(path_to_book))
    print("============ BOOKBOT ============")
    print (f"Analyzing book found at {path_to_book}...")
    print ("----------- Word Count ----------")
    print (f"Found {word_number} total words")
    print ("--------- Character Count -------")
    sorted_list(char_dict)
    print ("============= END ===============")

if len(sys.argv)!= 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])