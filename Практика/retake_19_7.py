n =  {"Вход": 5, "Профиль": 0, "Поиск": 2}
n ["Оплата"] = 1
n ["Вход"] = 0
print(n)
for module, count in n.items():
    if count > 0:
        print(f"Модуль: {module}, ошибок: {count}")
result = n.get("Настройки", "Нет данных")
print(f"Поиск модуля 'Настройки': {result}")
set1 = {"Вход", "Профиль"}
set2 = {"Профиль", "Оплата"}
peresechenie = set1 & set2
union = set1 | set2
print(set1)
print(set2)
print(peresechenie)
print(union)