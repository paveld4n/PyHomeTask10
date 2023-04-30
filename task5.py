# Задание 5.

# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
# преобразовать результаты из байтовового в строковый тип на кириллице.

# Подсказки:
# --- используйте модуль chardet, иначе задание не засчитается!!!


import subprocess
import chardet

arg_1 = ["ping", "yandex.ru"]
arg_2 = ["ping", "youtube.com"]
print("Пинг сайта yandex.ru")
ping_1 = subprocess.Popen(arg_1, stdout=subprocess.PIPE)
for line in ping_1.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
print("Пинг сайта youtube.com")
ping_2 = subprocess.Popen(arg_2, stdout=subprocess.PIPE)
for line in ping_2.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))