# 3

# 2
# 1 2
# 1000

# 3
# 1 5 10
# 100

# 2
# 5 7
# 22

import sys
N = int(input())

for _ in range(N):
    M = int(input())
    coin = list(map(int,input().split()))
    coin.insert(0, 0)  
    K = int(input())
    
    dp = [[0]*(K+1) for i in range(M+1)]
    
    for i in range(M+1):
        dp[i][0] = 1
    
    for j in range(1, M+1):
        for i in range(1, K+1):
            
            dp[j][i] = dp[j-1][i]
            
            if i-coin[j] >= 0:
                dp[j][i] += dp[j][i-coin[j]]
    print(dp[M][K])