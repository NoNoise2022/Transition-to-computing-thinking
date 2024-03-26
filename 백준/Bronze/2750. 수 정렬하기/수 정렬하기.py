# x = int(input())
# num_list = []

# for i in range(x):
#     num_list.append(int(input()))

# num_list1 = sorted(num_list)

# for i in range(len(num_list)):
#     print(num_list1[i])



# n = int(input())
# print(n)

# a = [0]*n

# for io in range(0,n):
#     a[io] = int(input())

# sorted(a)

# for i in a:
#     print(i)



N = int(input())
# A = list(map(int,input().split()))

# x = int(input())
A = []

for i in range(N):
    A.append(int(input()))


for i in range(N-1):
    # print(i)
    for j in range(N-1-i):
        # print(j)
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]

for num in A:
    print(num)
