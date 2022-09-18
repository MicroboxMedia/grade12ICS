import random

W = random.randint(-10, 10)
X = random.randint(-10, 10)
Y = random.randint(-10, 10)
Z = random.randint(-10, 10)

for _ in range(3):
    if W > X:
        W, X = X, W
    elif W > Y:
        W, Y = Y, W
    elif W > Z:
        W, Z = Z, W
for _ in range(2):
    if X > Y:
        X, Y = Y, X
    elif X > Z:
        X, Z = Z, X
if Y > Z:
    Y, Z = Z, Y
print(W, X, Y, Z)
