## Counting primes

Write a function `count_primes(start, stop)` which counts the number of prime numbers between `start` and `stop` (inclusive). A prime number is a number that is only divisible by 1 and itself. 

Example: `count_primes(5, 11)` should return `3` (5, 7, 11 are all prime). 

Note: 1 is not considered a prime number.

## Hints

* There are many interesting algorithms for checking whether a number is prime. For this problem, use the most 
  straightforward (and inefficient) approach: try to divide a number by every other number between 2 and the number,
  and check to see if there is a remainder left over for any of the divisors.
* Consider writing a helper function which determines whether a number is prime or not.
* Remember the "modulo" operator - `%`, which gives you the remainder.