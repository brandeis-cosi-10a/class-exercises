def a():
    print("a1")
    b()
    print("a2")
    c()
    print("a3")
    
def b():
    print("b1")
    c()
    print("b2")
    
def c():
    print("c1")
    d()
    print("c2")

def d():
    print("d")

a()
