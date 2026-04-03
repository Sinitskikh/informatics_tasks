# Задание 10. "Система учета склада"

"""
Задание: Создать систему учета материалов с контролем критических остатков
Цель: Изучение работы с объектами и вложенными словарями
"""

warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15}
}

print("=" * 60)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("-" * 60)
print(f"{'Материал':<10} | {'Кол-во':<6} | {'Цена':<8} | {'Мин.':<5} | {'Стоимость'}")
print("-" * 60)

total_value = 0
most_expensive_name = ""
max_cost = 0
critical_items = []

for name, info in warehouse.items():
    qty = info["quantity"]
    price = info["price"]
    min_qty = info["min_quantity"]
    cost = qty * price
    total_value += cost
    if cost > max_cost:
        max_cost = cost
        most_expensive_name = name

    critical_str = ""
    if qty < min_qty:
        critical_str = "⚠ КРИТИЧ!"
        critical_items.append(f"- {name}: {qty} < {min_qty}")

    print(f"{name:<10} | {qty:<6} | {price:<8.2f} | {min_qty:<5} | {cost:<10.2f} {critical_str}")

print("-" * 60)
print(f"ОБЩАЯ СТОИМОСТЬ: {total_value:.2f} руб")
print(f"Самый дорогой: {most_expensive_name} ({max_cost:.2f} руб)")

print(f"\n⚠ КРИТИЧЕСКИЕ ОСТАТКИ ({len(critical_items)}):")
for item in critical_items:
    print(item)

print("\n=== ВЫДАЧА МАТЕРИАЛА ===")
target = "Цемент"
to_take = 25

if target in warehouse:
    old_qty = warehouse[target]["quantity"]
    if old_qty >= to_take:
        warehouse[target]["quantity"] -= to_take
        print(f"✓ Выдано {to_take} единиц '{target}'")
        print(f"Остаток: {old_qty} -> {warehouse[target]['quantity']}")
    else:
        print("Недостаточно на складе!")