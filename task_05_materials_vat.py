# Задание 5. Калькулятор скидки

"""
Задание: Рассчитайте стоимость покупки материалов с прогрессивной системой скидок
Цель: Изучение арифметических операций и работы переменных
"""

# Инициализируем стартовые значения
price = 2000.0
quantity = 2
print("Стоимость: " + str(price) + " Количество: " + str(quantity))

# Вычисляем общую стоимость
total_price = price * quantity
print("Итого: " + str(total_price))

# Реализуем логику скидок
if total_price >= 1000 and total_price <= 5000:
    print("Скидка 5%")
    final_price = total_price - (total_price*0.05)
elif total_price >= 5000:
    print("Скидка 10%")
    final_price = total_price - (total_price*0.1)
else:
    print("Скидки нет")
    final_price = total_price

print(final_price)