n, m = 4, 5

graph = [
[int(i) for i in '00110'], 
[int(i) for i in '00011'], 
[int(i) for i in '11111'], 
[int(i) for i in '00000'], 
]

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)