from stats import word_count
from stats import num_char
from stats import sorted_list
import sys


# If sys.argv doesn't have two entries:
# Print a message explaining how to use the program: Usage: python3 main.py <path_to_book>
if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

# Use the second argument in sys.argv as the path to the book file.

def main():
    # frank = get_book_text("./books/frankenstein.txt")
    # print(frank)
    num_words = word_count(sys.argv[1])
    char_counts=num_char(sys.argv[1])
    char_dict = sorted_list(char_counts)
    print(f"Found {num_words} total words")
    # print(char_counts)
    for dic in char_dict:
        for key, value in dic.items():
            print(f"{key}: {value}")

# def get_book_text(file):
#     with open(file) as f:
#         file_contents = f.read()
#     return file_contents


        

main()
