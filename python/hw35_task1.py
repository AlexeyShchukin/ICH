"""1. Напишите функцию get_response(url), которая отправляет GET-запрос по заданному
URL-адресу и возвращает объект ответа. Затем выведите следующую информацию об ответе:
- Код состояния (status code)
- Текст ответа (response text)
- Заголовки ответа (response headers)"""

from requests import get


def get_response(url_string: str):
    return get(url_string)


url = "https://google.com"

response = get_response(url)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
print("Response Headers:", response.headers)
