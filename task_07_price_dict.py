# Задание 7. Прайс-лист материалов

"""
Задание: Работа со словарем
Цель: Изучение добавления, изменения, удаления, статистики
"""

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

print("")

materials_dict["Краска"] = 155
materials_dict["Плитка"] = 160

materials_dict["Газобетон"] = materials_dict["Газобетон"] + materials_dict["Газобетон"]*0.1

del materials_dict["Дерево"]

average_price = sum(materials_dict.values())/len(materials_dict)

print("Финальный список")
for key, value in materials_dict.items():
    print(key, value)
print("")
print("Средняя цена: " + str(average_price))
