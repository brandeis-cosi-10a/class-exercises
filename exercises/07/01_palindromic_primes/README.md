## Palindromic primes

A "palindromic prime" is a number that is both prime (only divisible by 1 and itself), and a palindrome (the same number when the order of the digits is reversed).

Write a function in [code.py](code.py) to find the `n`th palindromic prime.

The first palindromic primes are: 2, 3, 5, 7, 11, 101, 131.

## Hints

1. Define (and test!) some helper functions: `is_prime` and `is_palindrome` first
1. For `is_palindrome`: Don't forget that negative indexing can help you count backward from the end of a string.
   * e.g. `s[-2]` will give you the second to last character in `s`
1. For `is_prime` - don't worry about efficiency. Just check to see whether any number between 2 and `n-1` can evenly divide `n`. There are many more efficient ways to check for prime-ness, but they aren't necessary for this problem.
