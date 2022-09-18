width = 17
height = 12.0
delimeter = '.'
Pi = 3.1415926535
r = 5

# Exercise 1
print("Exercise 1")
print(width/2)
print(width/2.0)
print(height/3)
print(1+2*5)
print(delimeter*5)

# Exercise 2
print("Exercise 2")
volume = 4/3*Pi*r**3
print(f'{volume:.1f}')

numofbooks = 60
cost = numofbooks * (24.95 * 0.4) + (3 + (0.75*numofbooks))
print(f'{cost:.2f}')

# Exercise 3
print("Exercise 3")
p = 110000
r = 0.072/12
n = 30 * 12

m = p * (r/(1-((1+r)**-n)))
print(f'{m:.2f}')

