import sys
from stats import word_count, character_count, sorted_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)
    num_words = word_count(file_contents)
    num_characters = character_count(file_contents)
    sorted_characters = sorted_dict(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for sorted_character in sorted_characters:
        if sorted_character["char"].isalpha():
            print(f"{sorted_character["char"]}: {sorted_character["num"]}")
    print("============= END ===============")
    
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


main()