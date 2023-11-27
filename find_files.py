from os import getcwd, walk, path
from time import time

search_dir = input('Введите имя каталога: ')
search_file = input('Введите имя файла: ')
print('\nВвели имя каталога:', search_dir)
print('Ввели имя файла:', search_file, end='\n\n')

'''Принимаем варианты ввода каталога'''
temp_dir = ['C:\\', 'c:\\', 'c://', 'c:/', 'C:', 'c:']
if search_dir in temp_dir:
    search_dir = 'C:\\'
    print('Каталог поиска: C:\ - (весь диск)', end='\n\n')
else:
    '''Без ввода - текущий каталог'''
    search_dir = getcwd()
    print('Каталог поиска:', search_dir, end='\n\n')

start = time()
result = []
count_all = 0
count_find = 0

'''Кортеж (адрес, директория, файл)'''
for addr, dirs, files in walk(search_dir):
    for file in files:
        count_all += 1
        if file == search_file:

            '''Полный путь к файлу'''
            full_path = path.join(addr, file)
            print('Найден файл:', full_path)
            count_find += 1
            result.append(full_path)
if count_find == 0:
    print('Файл не найден')
stop = time()

'''Время на поиск в секундах'''
timer = int(stop - start)

print()
print(f'Время выполнения поиска: {timer // 60}мин. {timer % 60}сек.')
print('Количество проверенных файлов:', count_all)
print('Количество найденных файлов:', count_find, end='\n\n')
print('Список найденных файлов:', result, end='\n\n')
