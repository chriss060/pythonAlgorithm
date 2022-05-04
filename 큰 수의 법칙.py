# N, M, K 입력 받기
n, m, k = map(int, input().split())

# N개 데이터 받기
data = list(map(int, input().split()))

count = int(m / (k + 1)) * k
count += m % ( k + 1 )

data.sort()

first = data[n-1]
second = data[n-2]

result = first * count
result += second * (m - count)

print(result)

