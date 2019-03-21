
# 欧几里得算法计算最大公因数


def Gcd(m, n):
    while n > 0:
        rem = m % n
        m = n
        n = rem
    return m


print(Gcd(3, 7))
