# Задание 3.

# Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

# Подсказки:
# --- используйте списки и циклы, не дублируйте функции
# --- обязательно!!! усложните задачу, "отловив" исключение,
# придумайте как это сделать

# list_1 = ["attribute", "класс", "функция", "type"]
# for word in list_1:    
#     bt = bytes(word, encoding="utf-8")
#     print(f"\nТип переменной: {type(bt)}")
#     print(f"Содержание переменной: {bt}")
    
list_2 = ["attribute", "класс", "функция", "type"]
for word in list_2:
    try:
        bt = bytes(word, encoding="ascii")
            
    except UnicodeEncodeError:
        print(f"\n Cлово '{word}' невозможно преобразовать через 'b'")
    else:
        print(f"\nТип переменной: {type(bt)}")
        print(f"Содержание переменной: {bt}")
