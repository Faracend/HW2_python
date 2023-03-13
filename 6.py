# Получаем целое число от пользователя и сохраняем в переменной input_number
input_number = int(input())

# Инициализируем переменную result значением 1
result = 1

# Запускаем цикл от 1 до input_number + 1
for n in range(1, input_number + 1):
    # Инициализируем переменную factorial значением 1
    factorial = 1

    # Запускаем вложенный цикл от 1 до n + 1
    for i in range(1, n + 1):
        # Умножаем factorial на i и сохраняем результат в factorial
        factorial *= i

    # Увеличиваем result на единицу, деленную на значение factorial
    result += 1 / factorial

# Выводим результат, округленный до пятого знака после запятой
print(round(result, 5))
