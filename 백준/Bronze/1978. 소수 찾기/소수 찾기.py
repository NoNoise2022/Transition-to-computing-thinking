n = int(input())
numbers = list(map(int, input().split()))

counter = 0

for num in numbers:
    if num <= 1:  # 0 and 1 are not prime
        continue
    is_prime = True
    for i in range(2, int(num**0.5) + 1):  # check divisibility up to square root of num
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        counter += 1

print(counter)