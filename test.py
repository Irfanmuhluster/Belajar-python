x = 5
for i in range(x):
    print(("0" * (1 + 2 * i)).center(0 + 2 * x),
          ("0" * (1 + 2 * i)).center(0 + 2 * x))
    # print(("1" * (5 + 2 * i)).center(1 + 2 * x))
y = 10
for i in reversed(range(y)):
    print(("0" * (1 + 2 * i)).center(0 + 2 * y))
