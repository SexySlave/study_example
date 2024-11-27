import requests
import json

# Задание 1: Получение данных
print("Задание 1:")
response_1 = requests.get('https://api.github.com/search/repositories', params={'q': 'html'})
print("Статус-код ответа:", response_1.status_code)
print("Содержимое ответа (JSON):")
print(json.dumps(response_1.json(), indent=2))  # Красивый вывод JSON

# Задание 2: Параметры запроса
print("\nЗадание 2:")
response_2 = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': 1})
print("Полученные записи:")
print(json.dumps(response_2.json(), indent=2))

# Задание 3: Отправка данных
print("\nЗадание 3:")
data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response_3 = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print("Статус-код ответа:", response_3.status_code)
print("Содержимое ответа:")
print(json.dumps(response_3.json(), indent=2))
