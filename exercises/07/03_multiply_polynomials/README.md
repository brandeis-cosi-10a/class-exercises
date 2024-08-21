## Background

A polynomial is a mathematical expression with constants, variables, exponents, and operations. See [this page](https://www.mathsisfun.com/algebra/polynomials.html) if you need a refresher on what a polynomial is.

An example polynomial is: 4x<sup>3</sup> + 7x + 5. 

## Problem

In this problem, you will be writing a program in [main.py](main.py) to multiply 2 polynomials. Polynomials will be represented as a list of their coefficients.

So 4x<sup>3</sup> + 7x + 5 would be represented by the list `[4, 0, 7, 5]` (notice the `0` for the "missing" x<sup>2</sup> term).

We will write a function `multiplyPolynomials(p1, p2)`, which takes two lists representing polynomials as described above, and returns the list representing the polynomial that is the product of `p1` and `p2`.

For example, `multiplyPolynomials([4, 0, 7, 5], [2, 5])` represents the problem (4x<sup>3</sup> + 7x + 5)(2x + 5). This equals 8x<sup>4</sup> + 20x<sup>3<sup> + 14x<sup>2</sup> + 45x + 25. So the function would return `[8, 12, 14, 45, 25]`.

To multiply two polynomials `p1` and `p2`, you do this:

1. Multiply each term in `p1` by each term in `p2`, then
1. Simplify by combining "like terms" - terms that have the same exponent for x.

Here are those steps for the example above:

1. Multiply each term in `p1` by each term in `p2`:

    * The first term in p1 is 4x<sup>3</sup>. Multiply this by each term in `p2`:
        * 4x<sup>3</sup> * 2x = 8x<sup>4</sup>
        * 4x<sup>3</sup> * 5 = 20x<sup>3</sup>

    * The second term in `p1` is 0, so we skip it.

    * The third term in `p1` is 7x. Multiply this by each term in `p2`:
        * 7x * 2x = 14x<sup>2</sup>
        * 7x * 5 = 35x

    * The fourth term in `p1` is 5. Multiply this by each term in `p2`:
        * 5 * 2x = 10x
        * 5 * 5 = 25

2. Simplify by gathering like terms
    * Gather all the terms we just produced: 8x<sup>4</sup> + 20x<sup>3</sup> + 14x<sup>2</sup> + 35x + 10x + 25
    * Simplify: 8x<sup>4</sup> + 20x<sup>3</sup> + 14x<sup>2</sup> + 45x + 25

So, the result of our function would be: `[8, 20, 14, 45, 25]`

## Hints

1. Remember that the lists only contain the coefficients and not the exponents.
1. The degree of the result (that is, the highest exponent) is the sum of the degrees of the two polynomials `p1` and `p2`. 
    * In the example, since the degree of `p1` is 3, and the degree of `p2` is 1, the degree of their product is 3 + 1, or 4.
    * The length of the coefficient list is 1 larger than the degree. Thus, the in the example, since the product is of degree 4, we need a list of length 5 for the coefficients.
1. It is very helpful to start with a list of 0's as your coefficients. 
    * In the example, that would be a list of five 0's, or [0] * 5.
1. Then, loop over each term in p1, for each of those, loop over each term in p2, and compute the product of those two terms, and add that coefficient into the corresponding index in the result (that list of 5 0's).
