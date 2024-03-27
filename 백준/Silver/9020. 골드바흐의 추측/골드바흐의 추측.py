# 백준 9020 골드바흐의 추측
def sosu(x):
  if x==1:
    return False
  for i in range(2, int(x**0.5) + 1):
    if x % i == 0:
      return False
  return True

t = int(input())
for i in range(t):
  n = int(input())

  # n을 반으로 쪼개서 생각
  a, b = n//2, n//2
  while a > 0:
    if sosu(a) and sosu(b):
      print(a, b)
      break  # a, b 둘 다 소수면 출력하고 끝.
      
    # 아니면 a는 1씩 빼주고 b는 1씩 더해줌
    else: 
      a -= 1
      b += 1