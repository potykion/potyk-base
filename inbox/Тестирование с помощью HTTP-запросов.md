#может_пригодится

# Тестирование с помощью HTTP-запросов

## Как выглядит и как с этим работать?
- Как файлик с расширением `.http` 
```http
### Получение токена

POST {{host}}/api-token-auth/ HTTP/1.1
content-type: application/json

{
    "username": "dav",
    "password": "1"
}

### Отчет

GET {{host}}/api-v3/flu-preventive-examinations/?start=2022-06-13&end=2022-06-13&format=excel&jwt={{token}}
```
- Запросы разделяем с помощью `###`
- Комменты пишем с помощью `#`

- POST-параметры в виде json передаем с помощью `content-type`-хедера
- GET-параметры передаем в виде `query`-строки

- Можно использовать переменные окружения (среды), аналогично postman
- Пример среды - `.json`-файлик:
```json
{
  "dev": {
    "host": "http://127.0.0.1:8000",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMSwidXNlcm5hbWUiOiJkYXYiLCJleHAiOjE2NTUyNDAyMDMsImVtYWlsIjoiIiwib3JpZ19pYXQiOjE2NTUxOTcwMDN9.UyLmG0DliZXWOxG6O4ajNv6RGoTGhSMg54HhdX9C7Ps"
  }
}
```
- Запускать можно в PyCharm - интерфейс располагает