def flipAndInvertImage(A):
    B = []
    for li in A:
        li = li[::-1]
        B.append(li)
    for i in B:
        for l in range(len(i)):
            q = i.pop()
            i.insert(0, q^1)
            # if q == 1:
            #     i.insert(0, 0)
            # else:
            #     i.insert(0, 1)
    return B


List = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
answer = flipAndInvertImage(List)
print(answer)



