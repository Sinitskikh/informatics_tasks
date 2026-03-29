# Задание 1. "Цифровой паспорт" объекта

"""
Задание: Создайте "цифровой паспорт" строительного объекта с использованием базовых типов данных.
Цель: Демонстрация работы с базовыми типами данных (str, int, float, bool)
"""

student_name = "Синицких Анастасия Александровна"
group_number = "3140801/52502"
project_name = "ЖК Наука"

floors = 9
height = 27.0
is_residential = True
construction_year = 2023

print(f"=== ПАСПОРТ СТРОИТЕЛЬНОГО ОБЪЕКТА ===")
print(f"Составитель: {student_name}")
print(f"Группа: {group_number}\n")
print(f"Объект: {project_name}")
print(f"Этажность: {floors} эт.")
print(f"Высота: {height} м")
if is_residential == True:
    print(f"Тип: Жилой")
else:
    print(f"Тип: Нежилой")

print(f"Год постройки: {construction_year}")