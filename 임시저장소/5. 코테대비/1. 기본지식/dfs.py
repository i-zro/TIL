graph_list = {1: set([2, 5, 9]),
              2: set([1, 3]),
              3: set([2, 4]),
              4: set([3]),
              5: set([1, 6, 8]),
              6: set([5, 7]),
              7: set([6]),
              8: set([5]),
              9: set([1, 10]),
              10: set([9])
              }
root_node = 1

def DFS(graph, root):   # 그래프와 시작점이 있을 때
    visited = []    # 가 본 노드 저장
    stack = [root]  # 가야할 노드 저장

    while stack:
        n = stack.pop() # 
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)

    return visited

print(DFS(graph_list, root_node))

