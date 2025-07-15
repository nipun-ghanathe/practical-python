# bounce.py
#
# Exercise 1.5

next_height: float = 100
for i in range(1, 11):
    next_height = round(next_height * (3 / 5), 4)
    print(i, next_height)
