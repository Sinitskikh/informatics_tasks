# Задание 6. Каталог материалов

"""
Задание: Работа со списками
Цель: Индексация, срезы, добавления, удаление элементов
"""

# Создаем список материалов
materials = ["Дерево", "Мрамор", "Кварц", "Пластик", "Бетон"]

# Выводим первый и последний элементы
print(materials[0])
print(materials[len(materials) - 1])

# Выводим элементы в середине списка
for i in range(1, len(materials) - 1):
    print(materials[i])

# Разделитель
print("")

# Добавляем два новых материала
materials.append("Камень")
materials.append("Стекло")

# Удаляем второй элемент
del materials[1]

# Выводим все элементы нового списка
for i in range(0, len(materials)):
    print(materials[i])