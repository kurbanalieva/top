# Запрашиваем данные у пользователя
purchase_amount = float(input("Введите сумму покупки (в долларах): "))
age = int(input("Введите ваш возраст: "))

# Начальная скидка — 0%
total_discount = 0

# Проверяем, превышает ли сумма покупки 100 долларов
if purchase_amount > 100:
    total_discount += 10  # Добавляем скидку 10%

# Проверяем, старше ли покупатель 65 лет
if age > 65:
    total_discount += 5  # Добавляем дополнительную скидку 5%

# Рассчитываем итоговую сумму с учётом всех скидок
discount_amount = purchase_amount * (total_discount / 100)
final_amount = purchase_amount - discount_amount

# Форматируем вывод с округлением до 2 знаков после запятой
formatted_purchase = f"${purchase_amount:.2f}"
formatted_final = f"${final_amount:.2f}"
formatted_discount = f"{total_discount}%"

# Выводим результаты
print("\nРезультаты расчёта:")
print(f"Исходная сумма покупки: {formatted_purchase}")
print(f"Общая скидка: {formatted_discount}")
print(f"Итоговая сумма к оплате: {formatted_final}")
