## Find the most prominent peak

In this exercise, you will write code to identify the most "prominent" peak in a mountain range. The prominence of a peak is a measure of how tall it is relative to surrounding peaks.

You will write a function, `find_most_prominent(heights)` which takes in a list of integers representing the terrain heights across a range of mountains. Your function should return the prominence of the most prominent peak, **and** its index in the array. 

A peak's prominence is defined as the minimum of: (`peak height - left neigbor height`) and (`peak height - right neighbor height`). The most prominent peak has the largest prominence value. A peak at the beginning or end of the array only has one neighbor.

## Details

* The return value of the function should be a 2-tuple: (<prominence>, <index>)
* An empty input list should produce `(None, None)`
* A list of length 1 should produce `(<height of only peak>, 0)`
* Ties in prominence should choose the first most-prominent peak in the list.

## Examples

Given the heights: `[1, 7, 8, 3, 10, 4, 5]`, the peak at index 4 (`10`) has the largest prominence - it is 7 higher than its left neighbor (`3`), and 6 higher than its right neighbor (`4`). The prominence of this peak is `6` (`min(10-3, 10-4)`).

Given the heights: `[10, 20, 15, 1, 8, 2, 4]`, the peak at index 4 (`8`) is the most prominent (even though it is not the tallest peak). It has a prominence of `6` (`min(8-2, 8-1)`).

Given the heights: `[10, 3, 13, 11, 5, 1]`, the peak at index 0 (`10`) is the most prominent. It has a prominence of `7` (`10-3`).