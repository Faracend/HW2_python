user_input = int(input("Введите число: "))  # Запросить у пользователя число

for divisor in range(2, user_input + 1):  # Проверка делителей от 2 до введенного числа
    if user_input % divisor == 0:  # Если число делится на делитель без остатка
        print("Делитель числа", user_input, ":", divisor)  # Вывод делителя на экран
        break  # Прекратить цикл, т.к. найден первый делитель
