
def count_lengths(words):
    counts = {}
    for word in words.split():
        word_len = len(word)
        if word_len in counts:
            counts[word_len] += 1
        else:
            counts[word_len] = 1
    print(counts)

count_lengths("Hello class this string has many words of similar lengths")

def count_lengths_sorted(words):
    counts = {}
    for word in words.split():
        word_len = len(word)
        if word_len in counts:
            counts[word_len] += 1
        else:
            counts[word_len] = 1

    sortable = []
    for word_len in counts:
        sortable.append((counts[word_len], word_len))
    sortable.sort(reverse=True)
    for entry in sortable:
        print(f"Length {entry[1]} has count {entry[0]}")

count_lengths_sorted("Hello class this string has many words of similar lengths")
