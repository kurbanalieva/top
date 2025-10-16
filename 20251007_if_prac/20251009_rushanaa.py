# Простой вариант
birth = int(input("Введите год рождения: "))
year = 2025
age =year - birth
print(f"Ваш возраст: {age} лет")

# Сложный вариант 
# дата (7 октября 2025)
year= 2025
day=7
month=10
# данные у пользователя
dmonth= int(input('ваш месяц:'))
dyear= int(input('ваш год:'))
dday= int(input('ваш день:'))
# Рассчитываем возраст
age=year-dyear
# Проверяем, прошёл ли день рождения в этом году
if dmonth > month :
     age -= 1
     if day > dday :
      age -= 1
print(f'ваш возрост: {age} лет')

