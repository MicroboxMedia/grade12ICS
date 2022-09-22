import random

counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for _ in range(10000):
    num = random.randint(0, 9)
    counts[num] += 1
for c in counts:
    percent_total = c / 10000
    print(f'{percent_total}')
print(counts)
