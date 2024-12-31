# Bookshop | [English](README.md) | [Русский](README.ru.md)

## Installation and Launch

1. Clone the repository:
```bash
git clone https://github.com/username/bookshop.git
cd bookshop
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate    # for Windows
```

3. Install dependencies:
```bash
pip install -r requirements/dev.txt   # install development dependencies
pip install -r requirements/prod.txt  # install production dependencies
```

4. Create .env file and configure environment variables:

5. Apply migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run the server:
```bash
python manage.py runserver
```