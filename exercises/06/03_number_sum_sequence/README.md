## Number sum sequence

Write a function, `ns_sequence(start, n)` that generates the `n`th number of a sequence with the following rules:

1. The sequence starts at any given number (the `start` parameter to `ns_sequence`).
1. The next number in the sequence is the sum of all the digits in the previous number, multiplied by the number of items generated in the sequence so far.

For example, when staring with 153:

0. 153
1. (1 + 5 + 3) * 1 = 9
2. (9) * 2 = 18
3. (1 + 8) * 3 = 27
4. (2 + 7) * 4 = 36
5. (3 + 6) * 5 = 45

Or, when starting with 2731:

0. 2731
1. (2 + 7 + 3 + 1) * 1 = 13
2. (1 + 3) * 2 = 8
3. (8) * 3 = 24
4. (2 + 4) * 4 = 24
5. (2 + 4) * 5 = 30


## Hints

1. You can iterate over the individual characters in a string with a `for` loop (we may not have explicitly covered this in class yet):
```
for c in s:
    print(f"{c}" is a character from {s}")
```