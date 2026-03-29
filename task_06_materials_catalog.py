# Задание 6. Каталог материалов

"""
Задание: Работа со списками
Цель: Индексация, срезы, добавления, удаление элементов
"""

materials = ["Дерево", "Мрамор", "Кварц", "Пластик", "Бетон"]

print(materials[0])
print(materials[len(materials) - 1])

for i in range(1, len(materials) - 1):
    print(materials[i])

print("")
materials.append("Камень")
materials.append("Стекло")

del materials[1]

for i in range(0, len(materials)):
    print(materials[i])