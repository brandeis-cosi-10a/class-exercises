# Call stack maze

Use the debugger to answer the following questions about the code in [main.py](main.py):

1. How many times is `b()` called?
   * `b()` is called 8 times
1. The 4th time `f()` is called, what are the values of `r`, `y`, and `z`?
   * `r` = 6, `y` = 3, `z` = 10.0
1. What is the call stack the first time `e()` is called?
   * a -> b -> g -> a -> b -> g -> a -> c -> e
1. What is the call stack the first time `d()` calls `c()`?
   * a -> b -> g -> a -> c -> d
1. What are the values of `r`, `y`, and `z` just before the program exits?
   * `r` = 2, `y` = 11, `z` = 1.7782794100389228
