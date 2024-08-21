import math
r = 10
z = 100
y = 0

def a():
    q = b()
    c(q)
    b()

def b():
    global r
    global y
    r -= 1
    if r > 0:
        f()
    if y < 3:
        g()
    return r % 2

def c(j):
    if j % 2 == 0:
        d()
    else:
        e()

def d():
    v = f()
    if v > 5:
        c(v)

def e():
    global z
    z = math.sqrt(z)
    if z > 5:
        g()

def f():
    global y
    y += 1
    return y

def g():
    a()

a()
print("All done!")