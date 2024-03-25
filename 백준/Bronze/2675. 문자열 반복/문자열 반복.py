
n = int(input())

for _ in range(n):
    # print('a')
    repetit, strin = input().split(' ')
    # print(repetit)
    # print(strin)
    
    repetit = int(repetit)
    for chr in strin:
        print(repetit*chr, end="")
    print()


# print("n")
# n = input()

# for i in n:
#     print("num")
#     num = input()
#     for j in i:
#         for z in j:
#             print(num)

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다.
# 각 테스트 케이스는 반복 횟수, 
# 문자열 s가 공백으로 구분되어 주어진다.
# s의 길이는 적어도 1.

# ex. input : 
            # 2
            # 3 ABC
# ex. output :
            # AAABBBCCC

# n정수를 받습니다. 
# 반복문
