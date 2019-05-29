def calPoints(ops):
    ans = []
    for i in ops:
        if i == "+":
            ans.append(int(ans[-1])+int(ans[-2]))
            # print(ans, "是+号")
        elif i == "D":
            ans.append(int(ans[-1]) * 2)
            # print(ans, "是D")
        elif i == "C":
            ans.pop()
            # print(ans, "是C")
        else:
            ans.append(int(i))
            # 无法判断负数是否为偶数
            print(ans, "是数字")
    print(ans)
    sum = 0
    for j in ans:
        sum += int(j)
    return sum


ops = ["-21", "-66", "39", "+", "+"]
qq = calPoints(ops)
print(qq)
