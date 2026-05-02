import sys

center = sys.argv[1]
points = sys.argv[2]

if len(sys.argv) != 3:
    print("Программа сработает только с 2-мя параметрами: "
          "\n файл с центром и радиусом элипса - center"
          "\n файл с координатами - points")
    sys.exit(1)

with open(center, 'r') as f:
    x0, y0 = map(float, f.readline().split())
    a, b = map(float, f.readline().split())

with open(points, 'r') as f:
    for line in f:
        if line.strip():
            x, y = map(float, line.split())

        value = ((x - x0) ** 2 / a ** 2) + ((y - y0) ** 2 / b ** 2)

        eps = 1e-9

        if abs(value - 1) < eps:
            result = 0
        elif value < 1:
            result = 1
        else:
            result = 2

        print(result)


