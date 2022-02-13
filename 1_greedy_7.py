move_idx = [
    (-2, -1), (-2, 1),
    (2, -1), (2, 1),
    (1, -2), (-1, -2),
    (1, 2), (-1, 2)
]
data = 'a1'

x = int(ord(data[0])) - int(ord('a'))
y = int(data[1]) - 1

result = 0
for idx in move_idx:
    nx = x + idx[0]
    ny = y + idx[1]
    
    if nx >= 0 and nx <= 7 and ny >= 0 and ny <= 7:
        result += 1
print(result)