"""Count words in file."""

txt_file = open('test.txt')
word_count = {}

for line in txt_file:
    line = line.rstrip()
    words = line.split(" ")

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

for word, number in word_count.items():
    print(word, number)


txt_file.close()
