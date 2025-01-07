def raise_to_power(base, exponent):
    print(base, exponent)
    if exponent == 0:
        return 1
    else:
        r = raise_to_power(base, exponent-1)
        print(r)
        return r * base

print(raise_to_power(3, 5))
