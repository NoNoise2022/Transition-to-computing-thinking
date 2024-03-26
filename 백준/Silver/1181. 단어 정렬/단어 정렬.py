import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
set_lst = set(lst)
lst = list(set_lst)
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)

# 반복문 사용
# set()의 사용
# list()의 사용
    
# sort(), sort(key = len) 의 사용
