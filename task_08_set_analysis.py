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

symmetric_diff = str(first_contractor.difference(second_contractor, third_contractor)) + str(second_contractor.difference(third_contractor, first_contractor))+str(third_contractor.difference(second_contractor, first_contractor))

print("Все уникальные элементы: " + str(symmetric_diff))

intersection = set(first_contractor).intersection(second_contractor, third_contractor)

print(intersection)

only_first_contractor = first_contractor.difference(second_contractor, third_contractor)
print(only_first_contractor)

s1, s2, s3 = set(first_contractor), set(second_contractor), set(third_contractor)
result = (s1 & s2 | s2 & s3 | s1 & s3) - (s1 & s2 & s3)
print(list(result))

