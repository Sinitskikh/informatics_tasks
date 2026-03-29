# Задание 4. Рабочий график

"""
Задание: Рассчитайте стоимость покупки материалов с прогрессивной системой скидок
Цель: Изучение арифметических операций и работы переменных
"""

price = 2000.0
quantity = 2
print("Стоимость: " + str(price) + " Количество: " + str(quantity))
total_price = price * quantity
print("Итого: " + str(total_price))

if total_price >= 1000 and total_price <= 5000:
    final_price = total_price - (total_price*0.05)
elif total_price >= 5000:
    final_price = total_price - (total_price*0.1)
else:
    final_price = total_price

print(final_price)