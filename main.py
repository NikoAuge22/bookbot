import sys

from stats import get_num_words
from stats import get_characters
from stats import sorted_characters



def main():
    #check sys.argv
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #book_path = "books/frankenstein.txt"
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = get_characters(text)
    character_count = sorted_characters(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #print(characters)
    for i in character_count:
        char = i["char"]
        if char.isalpha():
            print(f"{i["char"]}: {i["num"]}")
        
    #print(character_count)
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()



main()
