# Ввод даты поступления на работу
print("Введите дату поступления: ")
start_year = (input("Год: "))
start_month = (input("Месяц: "))
start_day = (input("День: "))

start_year = int(start_year)
start_month = int(start_month)
start_day = int(start_day)
# Текущая дата
current_year = 2025
current_month = 10
current_day = 16

# Начальная зарплата
initial_salary = 50000

# Расчет количества месяцев работы
months_worked = 0
if start_year < current_year:
    months_worked = (current_year - start_year) * 12
elif start_month < current_month:
    months_worked = (current_month - start_month)
elif start_day < current_day:
    months_worked += 1

# Накопленные дни отпуска 
days = months_worked // 2 * 2

# Итоговая зарплата 
final_salary = initial_salary + (months_worked * 100)

# Расчет отпускных
pay = final_salary

# Вывод результатов
print(f"\nНакоплено дней отпуска: {days}")
print(f"Сумма отпускных: {pay} рублей")
print(f"Текущая зарплата: {final_salary} рублей") 