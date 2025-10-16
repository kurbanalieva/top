age = int(input("Введите возраст посетителя: "))
    
if age < 5:
    price = 0
elif 5 <= age <= 17:
    price = 10
else:
    price = 20
        
if price == 0:
    print("Вход бесплатный.")
else:
    print(f"Стоимость входного билета: {price} долларов.")
        
