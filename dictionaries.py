from collections import Counter

with open('textfile.txt', 'r') as file:
    text = file.read()

words = text.split()
word_count = Counter(words)
most_common_words = word_count.most_common(5)

for word, count in most_common_words:
    print(f"'{word}': {count}")
