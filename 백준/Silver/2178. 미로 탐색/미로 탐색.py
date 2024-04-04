# 4 6
# 101111
# 101010
# 101011
# 111011

from collections import deque
import sys
input = sys.stdin.readline


n,m = map(int,input().split())
graph = []

for _ in range(n):
    row = list(map(int,input().strip()))
    graph.append(row)

queue = deque([(0,0)])
dx = [1,-1,0,0]
dy = [0,0,-1,1]

while queue:
    x,y = queue.popleft()
    for i in range(4):
        next_x, next_y = x+dx[i], y+dy[i]
        if 0<=next_x<n and 0<=next_y<m:
            if graph[next_x][next_y] ==1:
                queue.append((next_x,next_y))
                
                graph[next_x][next_y] = graph[x][y]+1
                
print(graph[n-1][m-1])

# from collections import deque

# n,m = map(int, input().split())
# graph = []

# for _ in range(n):
#     row = list(map(int,input().strip()))
#     graph.append(row)
    
# queue = deque([(0,0)])

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# while queue:
#     x,y = queue.popleft()
    
#     for i in range(4):
#         next_x, next_y = x+dx[i], y+dy[i]
        
#         if 0<=next_x<n and 0<=next_y<m:
#             if graph[next_x][next_y] == 1:
#                 queue.append((next_x,next_y))
                
#                 graph[next_x][next_y] = graph[x][y]+1
                
# print(graph[n-1][m-1])