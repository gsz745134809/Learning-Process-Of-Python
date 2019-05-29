# 并查集：（ union & find ）

# 是一种树型的数据结构，用与处理一些不交集（Disjoint Sets）的合并及查询问题

# Find：确定元素属于哪一个子集。它可以被用来确定两个元素是否属于同一个子集

# Union：将两个子集合并成同一个集合


# 在生活中的例子：
# 1、 小弟 --> 老大
# 2、 帮派识别
# 3、 两种优化方式


# 并查集代码

function MakeSet(x)
    x.parent: = x
function Find(x)
    if x.parent == x
        return x
    else
        return Find(x.parent)
function Union(x, y)
    xRoot: = Find(x)
    yRoot: = Find(y)
    xRoot.parent: = yRoot


# 并查集优化
function MakeSet(x)
    x.parent: = x
    x.rank: = 0

function Union(x, y)
    xRoot: = Find(x, y)
    yRoot: = Find(x, y)
    if xRoot == yRoot
        return

    # x 和 y 不在同一个集合，合并它们

    if xRoot.rank < yRoot.rank
        xRoot.parent: = yRoot
    else if xRoot.rank > yRoot.rank
        yRoot.parent: = xRoot
    else
        yRoot.parent: = xRoot
        xRoot.rank: = xRoot.rank + 1
