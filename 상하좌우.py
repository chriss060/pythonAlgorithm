# N : 공간 크기 (n x n)

n = int(input())

plans = input().split()
move = ['L', 'R', 'U', 'D']

x , y = 1, 1

# 좌표 변화량 : L R U D
dx = [0, 0, -1, 1 ]
dy = [-1, 1 , 0 , 0]

for plan in plans:
    for i in range(len(move)):
     if plan == move[i]:
        nx = x + dx[i]
        ny = y + dy[i]

    if nx < 1 or ny < 1 or nx> n or ny > n:
        continue

    x , y = nx, ny

print(x, y)
