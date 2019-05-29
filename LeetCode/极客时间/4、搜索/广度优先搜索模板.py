# BFS


def BFS(graph, start, end):
    queue = []
    queue.append([start])
    visited.add(start)  # 添加到被访问过表里

    while queue:
        node = queue.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)  # 后继节点
        queue.push(nodes)
