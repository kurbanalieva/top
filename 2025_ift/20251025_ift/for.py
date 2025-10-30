#Запросить у пользователя число.
k = input('чесло: ')
k = int(k)
if k % 2 == 0:#(Оператор % — это остаток от деления.

#number % 2 вычисляет остаток от деления числа на 2.

#Примеры:

#4 % 2 → 0 (остаток 0 → чётное);

#5 % 2 → 1 (остаток 1 → нечётное).)

    #Вывести «Чётное», если число делится на 2,
    print('чет')
else:
    #иначе — «Нечётное».

    print('нечет:')
print('\n')

print('#2')

l = input('ch: ')
l = int(l)
o = input('ch:')
o = int(o)
print(l*o)
print('\n')


# Проверка формата
if ':' not in timeinput or len(timeinput.split(':')) != 2:
    print('Ошибка: введите время в формате ЧЧ:ММ (например, 16:55)')
else:
    hours, minutes = timeinput.split(':')
    hour = int(hours)
    minute = int(minutes)

   # Проверяем корректность времени
    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        print('Ошибка: введите время от 00:00 до 23:59')
    else:
        # Определяем время суток по часам 
            time_of_day = 'утро'
            greeting = 'Доброе утро!'
        elif 12 <= hour < 17:
            time_of_day = 'день'
            greeting = 'Добрый день!'
        elif 17 <= hour < 21:
            time_of_day = 'вечер'
            greeting = 'Добрый вечер!'
        else:  # 21–4 часа
            time_of_day = 'ночь'
            greeting = 'Спокойной ночи!'

        # Формируем ответ
        print(f'О, уже {time_of_day}! {greeting}')
