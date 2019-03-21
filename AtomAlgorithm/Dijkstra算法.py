'''
这里重述一下，狄克斯特拉算法包含4个步骤。
(1) 找出最便宜的节点，即可在最短时间内前往的节点。
(2) 对于该节点的邻居，检查是否有前往它们的更短路径，如果有，就更新其开销。
(3) 重复这个过程，直到对图中的每个节点都这样做了。
(4) 计算最终路径。（下一节再介绍！）
'''
# 狄克斯特拉算法只适用于有向无环图（directed acyclic graph，DAG）


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        # 遍历所有的节点
        cost = costs[node]
        if cost < lowest_cost and not in processed:
            # 如果当前节点的开销更低且未处理过，
            lowest_cost = cost  # 就将其视为开销最低的节点
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)  # 在未处理的节点中找出开销最小的节点
while node is not None:
    # 这个while循环在所有节点都被处理过后结束
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        # 遍历当前节点的所有邻居
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            # 如果经当前节点前往该邻居更近
            costs[n] = new_cost  # 就更新该邻居的开销
            parents[n] = node  # 同时将该邻居的父节点设置为当前节点
    processed.append(node)  # 将当前节点标记为处理过
    node = find_lowest_cost_node(costs)  # 找出接下来要处理的节点，并循环
