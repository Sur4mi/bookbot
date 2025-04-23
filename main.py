from stats import word_count
from stats import num_char
from stats import sorted_list
import sys

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def main():
    num_words = word_count(sys.argv[1])
    char_counts=num_char(sys.argv[1])
    char_dict = sorted_list(char_counts)
    print(f"Found {num_words} total words")
    for dic in char_dict:
        for key, value in dic.items():
            print(f"{key}: {value}")


main()
