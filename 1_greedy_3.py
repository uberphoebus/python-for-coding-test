data = '02984'
data = [int(i) for i in data]

result = data[0]
for i in range(len(data) - 1):
    if data[i] <= 1 or data[i + 1] <= 1:
        result += data[i + 1]
    else:
        result *= data[i + 1]

print(result)