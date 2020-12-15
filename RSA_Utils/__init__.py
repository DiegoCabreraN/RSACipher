def MaximumCommonDivisor(a, b):
    if a is not b:
        n = FindMaxN(a, b)
        return MaximumCommonDivisor(b, a-(n*b))
    return a


def FindMaxN(a, b):
    n = 1
    while (n+1)*b < a:
        n += 1
    return n


def SelectEpsilon(fi):
    e = 2
    mcd = MaximumCommonDivisor(fi, e)
    while mcd > 1:
        mcd = MaximumCommonDivisor(fi, e+1)
        e += 1
    return e


def FindEpsilonInverse(e, fi):
    inverse = 1
    for i in range(1, fi+1):
        product = e * i
        if product % fi == 1:
            inverse = i
            break
    return inverse
