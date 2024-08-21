def is_anagram(s1, s2):
    for c in s1:
        if s1.count(c) != s2.count(c):
            return False
    return True

def test_anagram():
    assert is_anagram("hello", "leloh")
    assert is_anagram("   ...", "...   ")
    assert is_anagram("HeLlO", "elLHO")
    assert not is_anagram("hello", "HELLO")
    assert not is_anagram("hello world", "helloworld")