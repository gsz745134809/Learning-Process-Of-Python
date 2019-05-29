def minDeletionSize(A):
    B = []
    m = []
    li = []
    count = 0
    for i in A:
        for j in range(len(A[0])):
            B += i[j]
    for q in range(len(A[0])):
        m.append(B[q::len(A[0])])
    for item in m:
        li = item
        if sorted(li) == item:
            continue
        else:
            count += 1
    return count


A = ["cba", "daf", "ghi"]
ans = minDeletionSize(A)
print(ans)
