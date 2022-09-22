d = {}

for i in range(1, 7):
    for j in range(1, 7):
        sums_list = []
        dice_rolls = (i, j)
        sum_of_dice = i + j
        sums_list.append(dice_rolls)
        if sum_of_dice not in d:
            d[sum_of_dice] = sums_list
        else:
            d[sum_of_dice] += sums_list

for dice_sum in d:
    print(f'{dice_sum:>2} {d[dice_sum]}')