import time
n, k = map(int, input().split())

count = 0

start_time = time.time()
while True:
    target = (n // k) * k
    count += (n - target)
    n = target

    if n < k :
        break
    # k로 나누기
    count += 1
    n //= k

count += (n-1)

end_time = time.time()

print(f'{count} : {end_time - start_time}')

