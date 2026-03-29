# Задание 3. Конвертер температур

"""
Задание: Переведите температуру из Цельсия в Фаренгейты и определите состояние воды.
Цель: Изучение ветвления и условий сравнения
"""

temperature_C = 232.8

temperature_F = temperature_C * 9/5 + 32

print("Температура по Цельсию: " + str(round(temperature_C, 2)) + "° равна " + str(round(temperature_F, 2)) + "° по Фаренгейту")

if temperature_C <= 0:
    print("Состояние воды - Лёд")
elif temperature_C > 0 and temperature_C < 100:
    print("Состояние воды - Жидкость")
else:
    print("Состояние воды - Пар")