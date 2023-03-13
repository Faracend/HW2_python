# Инициализируем пустую строку для хранения вводимых цифр
digits = ""

# Бесконечный цикл для ввода цифр пользователем
while True:
    digit = input()

    # Если цифра равна "0", то выходим из цикла
    if digit == "0":
        break
    else:
        # Добавляем введенную цифру к строке
        digits += digit

# Инициализируем переменную для хранения максимального значения
max_digit = 0

# Проходим по каждой цифре в строке
for d in digits:
    # Если это первая цифра, то присваиваем ее значение переменной max_digit и продолжаем цикл
    if max_digit == 0:
        max_digit = int(d)
        continue
    # Если текущее значение больше максимального, то присваиваем его значение переменной max_digit
    if int(d) > max_digit:
        max_digit = int(d)

# Выводим количество максимальных значений в строке
count_max_digit = digits.count(str(max_digit))
print(count_max_digit)