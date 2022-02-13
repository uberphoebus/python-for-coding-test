data = 'K1KA5CB7'

alp = []
val = 0
for i in data:
    if i.isalpha():
        alp.append(i)
    else:
        val += int(i)

alp = ''.join(sorted(alp))
print(alp + str(val))