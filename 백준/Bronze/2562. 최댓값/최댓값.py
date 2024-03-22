import sys  
#n = input()  
# a = [sys.stdin.readline() for i in range(n)]  

a = []
for i in range(9):
    a.append(int(sys.stdin.readline()))

#a = [3, 29, 38, 12, 57, 74, 40, 85, 61]

maxi = 0
count = 0

for i in range(len(a)):
    if maxi<a[i]:
        maxi = a[i]
        count = i+1
print(maxi)
print(count)