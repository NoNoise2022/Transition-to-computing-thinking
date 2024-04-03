from collections import deque
import sys
input_ = sys.stdin.readline  # 변수명을 input으로 하지 않도록 수정

N, M = map(int, input().split())  # splitO가 올바른 문법이 아니라 split()으로 수정
# 2차원 리스트 생성
graph = [list(map(int, ''.join(input().split()))) for _ in range(N)]  # 괄호와 split(), join 부분 수정

queue = deque([(0, 0)])
# 미로 문제 풀 때는 이동을 표현해준다.
dx = [0, 0, 1, -1]  # 변수명 수정
dy = [1, -1, 0, 0]  # 변수명 수정

# BFS
while queue:
    x, y = queue.popleft()  # 변수명 수정
    for i in range(4):
        next_x, next_y = x + dx[i], y + dy[i]  # 변수명 수정
        if 0 <= next_x < N and 0 <= next_y < M:  # 비교 연산자 수정
            if graph[next_x][next_y] == 1:  # 경로 확인
                queue.append((next_x, next_y))
                graph[next_x][next_y] = graph[x][y] + 1  # value 자체를
# print(graph[N-1JLM-1]) 수정
print(graph[N-1][M-1])
