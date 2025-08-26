# Тестовое задание для Pusto studio

## Технологии

Python 3.11 , Django 5.1, djangorestframework 3.15, Postgres 13, Nginx 1.25

## Реализовано:
 - Описаны модели Boost и Player(расположение game\backend\base\models.py).
 - Реализован метод начисления игроку приза за прохождение уровня(расположение game\backend\base\serializers.py).
 - Реализована выгрузка данных из базы данных в CSV-файл(расположение game\backend\base\utils.py).
## Запуск проекта

- Создать файл .env в папке infra и прописать в него свои данные.
Пример:
```
TOKEN=project_token
DB_ENGINE=django.db.backends.postgresql
POSTGRES_PASSWORD=postgres
POSTGRES_USER=postgres
POSTGRES_DB=postgres
POSTGRES_PORT=5432
POSTGRES_SERVER=db
```
- Запустить сборку  проекта:
```
cd infra
```
```
docker-compose up -d
```