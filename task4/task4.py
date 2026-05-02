import sys

if len(sys.argv) != 2:
    print(f"Программа сработает только с одним параметром "
          "\n запуск: python task4.py example1.txt")

    sys.exit(1)

example = sys.argv[1]

#example_array = []
with open(example, 'r') as f:
    example_array = [int(line.strip()) for line in f]
    # for line in f:
    #     example_array.append(list(map(int, line.split())))

example_array.sort()

median = len(example_array) // 2

steps = 0
for i in example_array:
    steps += abs(i - example_array[median])

    if steps > 20:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")
        sys.exit(1)

print(f"Минимальное количество ходов: {steps}")

