from curses.ascii import isupper


password = "0123456789"
num_of_nums = 0
num_of_upper = 0
num_of_lower = 0
num_of_symbols = 0

if len(password) < 8:
    print("Password is not long enough")

for char in password:
    if char.isupper():
        num_of_upper += 1
    elif not isinstance(char, int):
        num_of_


