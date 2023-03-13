total_sum = 0
count = 0
while True:
    user_input = int(input("Введите число (0 для окончания ввода): "))
    if user_input != 0:
        total_sum += user_input
        count += 1
    else:
        break

if count != 0: # Проверим, что было введено хотя бы одно число, чтобы избежать деления на ноль
    average = total_sum / count
    print(f"Среднее арифметическое: {average:.2f}")
