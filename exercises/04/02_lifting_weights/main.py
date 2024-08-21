#### Part 1 

def can_lift(name, weight_grams):
    if weight_grams < 0.25:
        print("An ant can lift a " + name)
    else:
        print("An ant cannot lift a " + name)

    if weight_grams < 28:
        print("A swallow can lift a " + name)
    else:
        print("A swallow cannot lift a " + name)

    if weight_grams < 120:
        print("A mouse can lift a " + name)
    else:
        print("A mouse cannot lift a " + name)

    if weight_grams < 6000000:
        print("An elephant can lift a " + name)
    else:
        print("An elephant cannot lift a " + name)

can_lift("coconut", 1000)
can_lift("boulder", 10000000)
can_lift("grain of sand", 0.1)


#### Part 2

def can_lift2(name, weight_grams):
    print("An ant can lift " + str(0.25 / weight_grams) + " " + name + "s")
    print("A swallow can lift " + str(28 / weight_grams) + " " + name + "s")
    print("A mouse can lift " + str(120 / weight_grams) + " " + name + "s")
    print("An elephant can lift " + str(6000000 / weight_grams) + " " + name + "s")

can_lift2("coconut", 1000)
can_lift2("boulder", 10000000)
can_lift2("grain of sand", 0.1)