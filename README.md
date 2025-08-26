# Тестовое задание для Pusto studio

## Технологии

Python 3.11 , Django 5.1, djangorestframework 3.15, Postgres 13, Nginx 1.25

## Реализовано:
 - Описаны модели Boost и Player(расположение game_test\backend\base\models.py).
 - Реализован метод начисления игроку приза за прохождение уровня(расположение game_test\backend\base\serializers.py).
 - Реализована выгрузка данных из базы данных в CSV-файл(расположение game_test\backend\base\utils.py).

## Запуск проекта

- Создать файл .env в папке infra и прописать в него свои данные.
Пример:
```
TOKEN=project_token
DB_ENGINE=django.db.backends.postgresql
POSTGRES_PASSWORD=db_password
POSTGRES_USER=db_user
POSTGRES_DB=db_name
POSTGRES_PORT=db_port
POSTGRES_SERVER=db_host_name
```
- Запустить сборку  проекта:
```
cd infra
```
```
docker-compose up -d
```