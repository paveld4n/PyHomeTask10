# Задание 2.

# Каждое из слов «class», «function», «method» записать в байтовом формате
# без преобразования в последовательность кодов
# не используя!!! методы encode и decode)
# и определить тип, содержимое и длину соответствующих переменных.

# Подсказки:
# --- b'class' - используйте маркировку b''
# --- используйте списки и циклы, не дублируйте функции

list_1 = ["class", "funktion", "method"]
for word in list_1:
    bt = bytes(word, encoding="utf-8")
    print(f"\nТип переменной: {type(bt)}")
    print(f"Содержание переменной: {bt}")
    print(f"Длина строки: {len(bt)}")