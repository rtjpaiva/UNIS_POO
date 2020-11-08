n = 100

print('\nEntre 1 e', n, 'são primos os números:\n')

x = 2

while x <= n - 1:
    y = 0
    z = 1

    while z < 100:
        if x % z == 0:
            y += 1
        z += 1

    if y == 2:
        print(x)

    x += 1