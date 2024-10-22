## Check for anagrams

Write a function, `is_anagram(s1, s2)` that returns `True` if `s1` and `s2` are anagrams. Anagrams are strings that contain the same characters, but not necessarily in the same order. 

### Details
* Ignore special characters, spacing, etc. For our purposes, anagrams contain **exactly** the same characters as each other, just in a (potentially) different order.
* Letters should only be considered equivalent if they are the same case - that is, `"aA"` should not be considered an anagram of `"Aa"`. 
* A string is always an anagram of itself.

You can use string's `count()` function. E.g. this code prints `2`:
```
val = "hello"
print(val.count("l"))
```

You should not use `sort()` for this problem.