# 1. Все четные числа от 0 до 1000
print("Четные числа:")
for num in range(0, 1001, 2):
    print(num, end=' ')
print("\n")

# 2. Все нечетные числа от 0 до 1000
print("Нечетные числа:")
for num in range(1, 1001, 2):
    print(num, end=' ')
print("\n")

# 3. Числа с цифрой 3
print("Числа с цифрой 3:")
for num in range(0, 1001):
    if '3' in str(num):
        print(num, end=' ')
print("\n")

# 4 
print("Трехзначные числа, кончающиеся на 7:")
for num in range(100, 1000):
    if num % 10 == 7:  # проверяем последнюю цифру
        print(num, end=' ')
print("\n")

print('5 не смогла')
print("\n")

# 6. Трехзначные числа без нуля
print("Трехзначные числа без нуля:")
for num in range(100, 1000):
    if '0' not in str(num):
        print(num, end=' ')
print("\n")

print('6 не смогла')
print("\n")

print('7 не смогла')
print("\n")

text = "мама мыла раму"
# Переворачиваем всю строку
letter = text[::-1]
print("Строка в обратном порядке букв:")
print(letter)
print("\n")

# 1 вариант
for num in range(77, 778, 2):
    print(num, end=' ')


start = 77
end = 777
step = 2
print("\n")

# Проверяем, чтобы начальное число было нечётным
if start % 2 == 0:
    start += 1

for num in range(start, end + 1, step):
    print(num, end=' ')
print("\n")

# Получаем ввод от пользователя
start = int(input("Введите начальное число: "))
end = int(input("Введите конечное число: "))

print("\n")
# Корректируем начальное число, если оно чётное
if start % 2 == 0:
    start += 1
print("\n")

# Выводим нечётные числа
for num in range(start, end + 1, 2):
    print(num, end=' ')

text = "Пример текста для демонстрации"
0

# Выводим каждый третий символ
result = text[::3]
print("\nКаждый третий символ:", result)


text = "Пример текста для демонстрации работы со словами"
words = text.split()

# Способ 1: срез списка
last_three_words = words[-3:]
print("\nТри последних слова (способ 1):", ' '.join(last_three_words))


# Способ 2: range
last_three_words = []
for i in range(len(words) - 3, len(words)):
    last_three_words.append(words[i])

print("Три последних слова (способ 2):", ' '.join(last_three_words))