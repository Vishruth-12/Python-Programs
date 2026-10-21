from collections import Counter
text = "practice makes progress and practice builds confidence"
for word, count in Counter(text.split()).most_common():
    print(f"{word}: {count}")