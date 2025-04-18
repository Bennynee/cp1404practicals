"""
Word occurrences
Estimates: 10 minutes
Actual: 15 minutes
"""
text = input("Text: ").strip()
words = text.split()
word_count = {}

for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_word_count = dict(sorted(word_count.items()))

max_length = max(len(word) for word in sorted_word_count)

for word, count in sorted_word_count.items():
    print(f"{word:<{max_length}} : {count}")
print()