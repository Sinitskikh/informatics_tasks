# Задание 8. Анализ заказов

"""
Задание: Использование множеств для анализа материалов трех подрядчиков
Цель: Изучение принципов работы с множествами
"""

first_contractor = {"Газобетон", "Кирпич керамический", "Кирпич силикатный", "ПВХ"}
second_contractor = {"Штукатурка", "Кирпич керамический", "Гидроизоляция", "Кирпич силикатный"}
third_contractor = {"Битумный праймер", "Кирпич керамический", "Краска", "Цемент"}

# все уникальные из общего списка
# unique = set(first_contractor+second_contractor+third_contractor)
# print(unique)

# Общий список элементов встречающихся только у одного подрядчика
symmetric_diff = str(", ".join(first_contractor.difference(second_contractor, third_contractor))) + ", " + str(", ".join(second_contractor.difference(third_contractor, first_contractor)))+", " +str(", ".join(third_contractor.difference(second_contractor, first_contractor)))
print("Все уникальные элементы: " + str(symmetric_diff))

# Пересечение у всех подрядчиков
intersection = set(first_contractor).intersection(second_contractor, third_contractor)
print("Общие во всех: " + str(", ".join(intersection)))

# Уникальное для первого подрядчика
only_first_contractor = first_contractor.difference(second_contractor, third_contractor)
print("Уникальные только в первом: " + str(", ".join(only_first_contractor)))

# Пересечение только у двух подрядчиков
s1, s2, s3 = set(first_contractor), set(second_contractor), set(third_contractor)
result = (s1 & s2 | s2 & s3 | s1 & s3) - (s1 & s2 & s3)
print("Общие только у двух: " + str(", ".join(result)))

