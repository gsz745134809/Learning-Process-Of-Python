from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == 'm'

def search(name):
    search_queue = deque()
    search_queue += graph[name]  # 此处graph[name]记录的是name的所有朋友
    searched = []  # 这个数组用于记录检查过的人

    while search_queue:  # 只要队列不为空
        person = search_queue.popleft()  # 就取出其中的第一个人
        if person not in searched:
            # 仅当这个人没检查过时才检查
            if person_is_seller(person):
                # 检查这个人是否是芒果销售商
                print(person+" is a mango seller!")  # 是芒果销售商
                return True
            else:
                search_queue += graph[person]  # 不是芒果销售商。将这个人的朋友都加入搜索队列
                searched.append(person)  # 将这个人标记为检查过
    return False

search("you")
