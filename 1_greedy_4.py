n = 5
data = list(map(int, '2 3 1 2 2'.split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)