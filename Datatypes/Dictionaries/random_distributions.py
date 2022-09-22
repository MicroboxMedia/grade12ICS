import random

numbers = {i: 0 for i in range(1, 11)}

for _ in range(1000):
    numbers[random.randint(1, 10)] += 1

print('Random number frequencies')
for j in range(1, 11):
    print(f'num {j:>2}, chosen {(numbers[j] / 1000 * 100):>2.0f}% of the time')
