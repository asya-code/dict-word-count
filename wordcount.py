
import sys

filename = sys.argv[1]
def tokenize(line):
    """Open file and generate list of each word"""
    line = line.rstrip()
    words = line.split(" ")
    return words


def words_count(filename):
    """Count words in file."""
    txt_file = open(filename)
    words_count = {}
    for line in txt_file:
        words = tokenize(line)

        for word in words:
            words_count[word] = words_count.get(word, 0) + 1

    txt_file.close()
    return words_count

def print_words_count(filename):
    """Print each key, value in dictionary"""

    words_counts = words_count(filename)

    for word, number in words_counts.items():
        print(word, number)


print_words_count(filename)