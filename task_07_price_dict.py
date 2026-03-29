# Задание 7. Прайс-лист материалов

"""
Задание: Работа со словарем
Цель: Изучение добавления, изменения, удаления, статистики
"""

# Создаем словарь и выводим его содержимое в удобном формате
materials_dict = {
    "Дерево": 125,
    "Кирпич силикатный": 165,
    "Штукатурка": 150,
    "Газобетон": 200,
    "Кирпич керамический": 170,
}
print("Начальный список")
for key, value in materials_dict.items():
    print(key, value)

# Разделитель
print("")

# Добавляем два элемента в словарь
materials_dict["Краска"] = 155
materials_dict["Плитка"] = 160

# Изменяем цену на Газобетон
materials_dict["Газобетон"] = materials_dict["Газобетон"] + materials_dict["Газобетон"]*0.1

# Удаляем материал
del materials_dict["Дерево"]

# Вычисляем среднюю цену
average_price = sum(materials_dict.values())/len(materials_dict)

# Выводим финальный список и среднюю цену
print("Финальный список:")
for key, value in materials_dict.items():
    print(key, value)
print("")
print("Средняя цена: " + str(average_price))
