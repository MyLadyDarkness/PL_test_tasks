import sys

def round_arr(n, m):
    current = 1
    fin_arr = []

    while True:
        step_arr = []
        value = current

        for _ in range(m):
            step_arr.append(value)

            if value == n:
                value = 1
            else:
                value += 1

        fin_arr.append(step_arr[0])
        if step_arr[-1] == 1:
            break

        current = step_arr[-1]
    return fin_arr


try:
    n1, m1, n2, m2 = map(int, sys.argv[1:])
except (IndexError, ValueError):
    print("Программа запустится только с 4-мя целочисленными параметрами: "
          "\n n1 -  конечное число для кругового массива 1"
          "\n m1 - интервал движения для массива 1"
          "\n n2 -  конечное число для кругового массива 2"
          "\n m2 - интервал движения для массива 2")

result = ''.join(map(str, round_arr(n1, m1) + round_arr(n2, m2)))
print(result)