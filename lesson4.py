print("Введите первую точку")

x1 = float(input('X: '))

y1 = float(input('Y: '))

print("\nВведите вторую точку")

x2 = float(input('X: '))

y2 = float(input('Y: '))

x_diff = x1 - x2
if x_diff != 0:
    y_diff = y1 - y2

    k = y_diff / x_diff

    b = y2 - k * x2

    print("Уравнение прямой, проходящей через эти точки:")

    print("y = ", k, " * x + ", b)
else:
    print('Прямая является вертикальной линией, проходящей через X =', x1)
# Further draw grafic of this function
x_start = int(input('Введите начальное знач-е X: '))
x_end = int(input('Введите конечное знач-е X: '))
y_start = int(k * x_start + b)
y_end = int(k * x_end + b)

for y in range(y_end+5, y_start-5, -1):
    for x in range(x_start-5, x_end+5, 1):
        if x == ((x_end+5) - (x_start-5)) // 2:
            print('|', end = '')
        elif y == ((y_end+5) - (y_start-5)) // 2:
            print('-', end = '')
        elif y == k * x + b:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()



x_user = float(input('Введите желаемую точку X: '))
print('Значение Y для', x_user, 'равняется', k * x_user + b)
