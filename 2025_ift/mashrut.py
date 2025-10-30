print('6 за')
for i in range(11,101,2):
    print(i,end=' ')
print('\n')

print("Двузначные числа с чётной суммой цифр:")
for num in range(10, 100):
    digit_sum = (num // 10) + (num % 10)  # десятки + единицы
    if digit_sum % 2 == 0:
        print(num, end=' ')
print()
