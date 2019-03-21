

def isEven(x):
    if x % 2 == 0:
        return False
    else:
        return True


def Pow(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x
    if n % 2 == 0:
        return Pow(x*x, n//2)
    else:
        return Pow(x*x, n//2)*x


print(Pow(3, 4))
