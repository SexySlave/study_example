from fuzzywuzzy import fuzz
from fuzzywuzzy import process

a = fuzz.ratio('Привет мир', 'Привет мир')
print(a)

a = fuzz.ratio('Привет мир', 'Привт кир')
print(a)
#Выводит в консоль: 84


a = fuzz.partial_ratio('Привет мир', 'Привет мир!')
print(a)
#Выводит в консоль: 100


a = fuzz.partial_ratio('Привет мир', 'Привет мир!')
print(a)
#Выводит в консоль: 100

a = fuzz.partial_ratio('Привет мир', 'Люблю колбасу, привет мир')
print(a)



a = fuzz.token_sort_ratio('Привет наш мир', 'мир наш Привет')
print(a)
#Выводит в консоль: 100


a = fuzz.token_sort_ratio('Привет наш мир', 'мир наш любимый Привет')
print(a)
#Выводит в консоль: 78


a = fuzz.token_sort_ratio('1 2 Привет наш мир', '1 мир наш 2 ПриВЕт')
print(a)
#Выводит в консоль: 100



a = fuzz.token_set_ratio('Привет наш мир', 'мир мир наш наш наш ПриВЕт')
print(a)
#Выводит в консоль: 100

a = fuzz.WRatio('Привет наш мир', '!ПриВЕт наш мир!')
print(a)
#Выводит в консоль: 100



a = fuzz.WRatio('Привет наш мир', '!ПриВЕт, наш мир!')
print(a)
#Выводит в консоль: 97

city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]
a = process.extract("Саратов", city, limit=2)
# Параметр limit по умолчанию имеет значение 5
print(a)
#Выводит в консоль: [('Саратов', 100), ('Самара', 62)]


city = ["Москва", "Санкт-Петербург", "Саратов", "Краснодар", "Воронеж", "Омск", "Екатеринбург", "Орск", "Красногорск", "Красноярск", "Самара"]
a = process.extractOne("Краногрск", city)
print(a)
#Выводит в консоль: ('Красногорск', 90)


# #открытие файла на рабочем столе
# try:
#     files = os.listdir('C:\\Users\\hartp\\Desktop\\')
#     filestart = process.extractOne(namerec, files)
#     if filestart[1] >= 80:
#         os.startfile('C:\\Users\\hartp\\Desktop\\' + filestart[0])
#     else:
#         speak('Файл не найден')
# except FileNotFoundError:
#     speak('Файл не найден')
# files = os.listdir('C:\\Users\\hartp\\Desktop\\')
# print(files)
# #Выводит в консоль: 'Visual Studio 2019.lnk', 'Visual Studio Code.lnk', 'WarThunder.lnk', 'WpfApp14', 'Yandex.lnk', 'Автобус.docx', 'Аэрофлот.txt', 'Для курсача.txt' и т.д.