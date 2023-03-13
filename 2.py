num_count = int(input("Введите количество чисел: "))  # Запросить у пользователя количество чисел
zero_found = False  # Создать флаг для отслеживания наличия нуля в последовательности

for i in range(num_count):
    number = int(input(f"Введите число {i + 1}: "))  # Запросить у пользователя число
    if number == 0:
        zero_found = True  # Если число равно 0, установить флаг на True

if zero_found:
    print("YES")
else:
    print("NO")
