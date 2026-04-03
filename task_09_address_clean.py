# Задание 9. "Очистка адресов"

"""
Задание: Привести адреса объектов к стандартному формату
Цель: Работа со строками
"""

addresses = [
    "  г. Москва, ул. Ленина, д. 10 ",
    "г.Казань,ул.Баумана,д.15",
    " г. Санкт-Петербург, ул. Невский, д. 100 "
]

cleaned_addresses = []

for addr in addresses:
    res = addr.strip()
    res = res.replace(" ,", ",").replace(",", ", ")
    res = res.replace("г.", "г. ").replace("ул.", "ул. ").replace("д.", "д. ")
    res = " ".join(res.split())
    res = res.replace(",  ", ", ")

    cleaned_addresses.append(res)

print("=== СРАВНЕНИЕ ===")
print("")

for index, item in enumerate(cleaned_addresses):
    print("#" + str(index + 1))
    print(f"ДО: '{addresses[index]}'")
    print(f"ПОСЛЕ: '{item}'")
    print("")


