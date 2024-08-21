def find_short_words(words, limit):
    new_words = []
    for word in words:
        if len(word) < limit:
            new_words.append(word)
    return new_words

def test_basic():
    assert find_short_words(["a", "and", "schedule", "but", "train"], 4) == ["a", "and", "but"]

def test_no_match():
    assert find_short_words(["only", "long", "words"], 3) == []

def test_all_match():    
    assert find_short_words(["only", "long", "words"], 6) == ["only", "long", "words"]
