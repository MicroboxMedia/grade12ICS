from random import randint


import random
def even_odd_list(number_values, low_value, high_value):
    step=(number_values+1)//2
    num_list = [random.randrange(low_value, high_value + 1, 2) for _ in range((number_values + 1) // 2)]

    num_list.extend(random.randrange(low_value, high_value + 1, 2) + 1 for _ in range((number_values) // 2))

    return num_list

print(even_odd_list(2,10,30))
