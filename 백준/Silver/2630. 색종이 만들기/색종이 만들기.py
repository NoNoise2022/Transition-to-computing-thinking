import sys

N = int(sys.stdin.readline())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
result = []

# print(N)
# print(paper)

def sol(x,y,N):
    color = paper[x][y]

    for i in range(x,x+N):
        # print(i, end=' ')
        for j in range(y,y+N):
            # print(j, end=' ')
            if color != paper[i][j] :
                sol(x, y, N//2)
                sol(x, y+N//2, N//2)
                sol(x+N//2, y, N//2)
                sol(x+N//2, y+N//2, N//2)
                return
    if color == 0 :
        result.append(0)
    else :
        result.append(1)

sol(0,0,N)

print(result.count(0))
print(result.count(1))

# 8
# 1 1 0 0 0 0 1 1
# 1 1 0 0 0 0 1 1
# 0 0 0 0 1 1 0 0
# 0 0 0 0 1 1 0 0
# 1 0 0 0 1 1 1 1
# 0 1 0 0 1 1 1 1
# 0 0 1 1 1 1 1 1
# 0 0 1 1 1 1 1 1