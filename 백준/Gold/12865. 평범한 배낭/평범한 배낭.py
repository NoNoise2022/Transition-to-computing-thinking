# 4 7
# 6 13
# 4 8
# 3 6
# 5 12


import sys
input = sys.stdin.readline

N, K = map(int, input().split())

bag = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]
#DP표는 0~K+1, 0~N+1로 구성하자 (N=1일 때, DP[i-1][j]가 존재해야 하므로)

for i in range(1,N+1):
    for j in range(1,K+1):
        if j >= bag[i-1][0]:  #"현재최대무게j가 해당물건무게보다 큰 경우
        #표의 윗 셀의 값과 현재물건의V+이전물건의V값의 최댓값을 DP[i][j]에 저장
            dp[i][j] = max(bag[i-1][1]+dp[i-1][j-bag[i-1][0]],dp[i-1][j])

            # print(f'bag[i-1][1] : {bag[i-1][1]}')
            # print(f'dp[i-1][j-bag[i-1][0]] : i: {i} j: {j} : {dp[i-1][j-bag[i-1][0]]}')
        else:
        	#"현재최대무게j가 해당물건무게보다 작은 경우 (현재 물건을 담을 수 없는 경우)
            dp[i][j] = dp[i-1][j]
            #print(f'dp[i][j] : i: {i} j: {j} : {dp[i][j]}', end=' ')
            #print(f'bag[i-1][1] : i: {i} j: {j} : {bag[i-1][1]}')

print(dp[N][K])  #DP[N][K]가 무조건 정답






# # W 배낭의 무게한도
# # wt 각 보석의 무게
# # val 각 보석의 가격
# # n 보석의 수
# def knap(W, wt, val, n):
    
#     K = []
#     for _ in range(n+1):
#         row = []
#         for _ in range(W+1):
#             row.append(0)
#         K.append(row)

    
#     for i in range(n+1):
#         for w in range(W+1):
            
#             if i==0 or w==0:
#                 K[i][w] = 0
                
#             elif wt[i-1] <= w:
#                 K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1[w]])
#             else:
#                 K[i][w] = K[i-1][w]
#     return K[n][W]

# wt = []
# val = []

# # N,K = map(int, input().strip().split())
# N,K = map(int, input().split())

# for i in range(N):
#     w,v = map(int,input().split())

#     wt.append(w)
#     val.append(v)
    
# print(knap(K, wt, val, N))
# # 첫번째 K 즉 무게한도
# # 두번쨰 wt 즉 빈 리스트
# # 세번째 val 즉 빈 리스트
# # 넷쨰 N 즉 입력 횟수

