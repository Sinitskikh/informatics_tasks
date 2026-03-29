# Задание 2. Параметры помещения

"""
Задание: Рассчитайте геометрические параметры помещения и стоимость покраски стен.
Цель: Демонстрация использования алгебраических функций.
"""

length = 10.5
width = 12.4
height = 3

walls = length*height + width*height
floor = width*length
volume = length*width*height

print("Площадь стен: " + str(round(walls, 2)))
print("Площадь пола: " + str(round(floor, 2 )))
print("Объем: " + str(round(volume, 2)))

price = round(walls*125, 2)

print("Стоимость покраски стен: " + str(price))