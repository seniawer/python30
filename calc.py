bill = float(input("Сумма чека: "))
percent = float(input("Процент чаевых: "))
tip = bill * percent / 100
total = bill + tip
print(f"Чаевые: {tip} руб")
print(f"Итого: {total} руб")