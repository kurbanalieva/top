material = input("ведите тип материала:")
while True:
    cost_input = input("Введите стоимость материала (в рублях): ")
    try:
        # Пытаемся преобразовать ввод в число
        cost = float(cost_input)
        if cost > 0:
            break  # Если число положительное — выходим из цикла
        else:
            print("Ошибка: стоимость должна быть положительным числом. Попробуйте ещё раз.")
    except ValueError:
        print("Ошибка: введите, пожалуйста, число. Попробуйте ещё раз.")
a = input('Категория:')  
print(material )
print(f"Стоимость: {cost} руб.")
print(a)