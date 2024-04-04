from collections import deque
n, m = map(int, input().split())
graph = []
data = []
queue = deque()
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], i, j))      
data.sort()
for d in data:
    virus, virus_x, virus_y = d
    queue.append((0, virus_x, virus_y))
    
t, X, Y  = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    time, x, y = queue.popleft()
    if time == t:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y]
                queue.append((time+1, nx, ny)) 
print(graph[X-1][Y-1])