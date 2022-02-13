# DFS : 깊이 우선 탐색
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 철
# 2. 스택 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드 꺼냄.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

graph = [
    [],
    [2, 3, 8], 
    [1, 7], 
    [1, 4, 5], 
    [3, 5], 
    [3, 4],
    [7], 
    [2, 6, 8], 
    [1, 7]
]

visited = [False] * 9

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

print(dfs(graph, 1, visited))