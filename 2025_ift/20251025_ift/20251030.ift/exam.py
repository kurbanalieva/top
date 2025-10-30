print('Задача №1')
#Запрашиваем у пользователя время.
hour = input('Который час?: ')
hour = int(hour)
#время когда надо спать 
bedtime = 22
#сколько часов осталось до сна.
sleep = bedtime -hour 
#некорректный час
if hour >= 22:
    print('уже пора спать!:')
else:
       print(f"До сна часов: {sleep}")
print('\n')

print('Задача №2')

time = input('Который час? (в формате ЧЧ:ММ): ')

# Проверяем формат ввода
if ':' not in time:
    print('Ошибка: введите время(например, 19:35)')
else:
    # Разделяем часы и минуты
    hours, minutes = time.split(':')
    hour = int(hours)
    minute = int(minutes)
    

    # Проверяем корректность времени
    if hour < 0 or hour > 23 or minute < 0 or minute > 59:
        print('Ошибка: введите время от 00:00 до 23:59')
    else:
        # Определяем время суток по часам (минуты влияют только на переходные границы)
        if 5 <= hour < 12:
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

        # ответ
        print(f'О, уже {time_of_day}! {greeting}')
print('\n')

print('Задача №3')

#Спрашиваем у  пользователя день его рождения
day = input("день вашего дня рождения?: ")
day = int(day)
#Спрашиваем у  пользователя месяц день его рождения
month = input('месяц вашего дня рождения?: ')
month = int(month)
# Текущая дата
current_month = 10
current_day = 30

if month < current_month:
    ckol = (current_month - month)
elif day < current_day:
    


