# 행 개수 N, 열 개수 M 받기
n, m = map(int, input().split())

lowest = [None] * n

for i in range(n):
    data = list(map(int, input().split()))
    lowest[i] = min(data)

result = max(lowest)
print(result)