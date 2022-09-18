max_num = 1
path_length = 0
n = 27

while n != 1:
    if n % 2 == 1:
        n = n*3+1
    else:
        n /= 2
    if n>max_num:
        max_num = n
    path_length += 1

print(path_length, max_num) 