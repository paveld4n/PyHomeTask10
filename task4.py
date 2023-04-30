# Задание 4.

# Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить
# обратное преобразование (используя методы encode и decode).

# Подсказки:
# --- используйте списки и циклы, не дублируйте функции

# list_1 = ["разработка", "администрирование»", "protocol", "standard"]
# print("Преобразование из строкового представления в байтовое")
# for word1 in list_1:
#     bt1 = word1.encode("utf-8")
#     print(f"Содержание переменной: {bt1}")
    

# list_2 = [b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0',\
#         b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5',
#              b'protocol', b'standard']
# print("\nПреобразование из байтового представления в строковое")
# for word2 in list_2:
#     bt2 = word2.decode("utf-8")
#     print(f"Содержание переменной: {bt2}")

list_1 = ["разработка", "администрирование»", "protocol", "standard"]
for word1 in list_1:
    bt1 = word1.encode("utf-8")
    print(f"Содержание переменной: {bt1}")
    str_1 = bt1.decode("utf-8")
    print(f"Содержание переменной: {str_1}")