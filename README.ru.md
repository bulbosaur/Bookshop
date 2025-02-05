# Bookshop | [English](README.md) | [Русский](README.ru.md)

## Установка и запуск

1. Клонируйте репозиторий:

```bash
git clone https://github.com/username/bookshop.git
cd bookshop
```
2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
venv\Scripts\activate  # для Windows
```

3. Установите зависимости:

```bash
pip install -r requirements/dev.txt   # установка зависимостей для разработки
pip install -r requirements/prod.txt  # установка продакшн зависимостей
```

4. Создайте файл .env:
```bash
DEBUG=true
SECRET_KEY="True"
```

5. Примените миграции:
```bash
python manage.py migrate
```

6. Создайте суперпользователя:

```bash
python manage.py createsuperuser
```

7. Запустите сервер:

```bash
python manage.py runserver
```


