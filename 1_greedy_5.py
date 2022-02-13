dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

x, y = 2, 2

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # print(nx, ny)


n = 5
plans = 'R R R U D D'.split()

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny

print(x, y)