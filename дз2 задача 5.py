n = 0

for i in range(32, 128):
    print(i , chr(i),end='')
    n += 1
    if n % 10 == 0:
        print()
