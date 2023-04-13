"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

yandex = ['ping', 'yandex.ru']
yan_x = subprocess.Popen(yandex, stdout=subprocess.PIPE)
print('yandex.ru')
for line in yan_x.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

youtube = ['ping', 'youtube.com']
you_b = subprocess.Popen(youtube, stdout=subprocess.PIPE)
print('youtube.com')
for line in you_b.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))