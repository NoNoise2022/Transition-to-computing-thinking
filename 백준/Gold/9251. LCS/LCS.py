X = input()
Y = input()

#abcbdab
#bcdb

# ACAYKP
# CAPCAK

C = [[0]*(len(Y)+1) for _ in range(len(X)+1)]

def lcs(m,n):
    for i in range(1,m+1):
        for j in range(1,n+1):

            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i-1][j], C[i][j-1])
    return C[m][n]

print(lcs(len(X),len(Y)))