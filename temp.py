f = open('input.txt')
n = f.readline()
n = int(n.split(':')[1])
f.readline();f.readline();f.readline()
line = f.readline()
items = []
while line:
    line = line.strip()
    x = line.split(':')
    x[1] = int(x[1])
    items.append(x)
    line = f.readline()
f.close()
items.sort(key = lambda x: x[1])
min_diff = items[-1][1]
min_index = 0
l = len(items)
for i in range(l-n+1):
    diff = items[i + n - 1][1] - items[i][1]
    if diff <= min_diff:
        min_diff = diff
        min_index = i
with open('output.txt', 'w') as f:
    f.write('Number of employees: ' + str(n) + '\n\n')
    f.write('Here the goodies that are selected for distribution are:' + '\n')
    for i in range(min_index, min_index + n):
        f.write(items[i][0] + ': ' + str(items[i][1]) + '\n')
    f.write('\n')
    f.write('And the difference between the chosen goodie with highest price and the lowest price is ' + str(min_diff))
