








from collections import deque
from sys import stdin
import heapq

import sys

input = sys.stdin.readline

N = int(input())
Q = []

for _ in range(N):
    x = int(input())

    if x == 0:
        if Q:
            print(-heapq.heappop(Q), end=' ')
        else:
            print(0, end=' ')
    else:
        heapq.heappush(Q, -x)
    

# # N = int(input())
# N = int(stdin.readline())
# lst = [None]*N
# smp = []

# for i in range(N):
#     K = int(stdin.readline())
#     lst[i] = K
#     # print(lst[i], end=' ')

# for j in range(lst):
#     # 리스트에서 요소가 나온다.
#     if j != 0:
#         # pass
#         smp.append(j)
#         lst.pop()
#     else:
#         pass
        