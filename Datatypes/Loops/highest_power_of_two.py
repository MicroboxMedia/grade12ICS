import random

target = random.randint(1, 10000)
two_p_plus_one = 4
power = 1

while target > two_p_plus_one:
    two_p_plus_one *= 2
    power += 1
print(f'The highest power of 2 is {power}{" for the number "}{target}')
