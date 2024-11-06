ПРОЕКТ "ОБРАЗОВАТЕЛЬНЫЕ МОДУЛИ
        Educational_modules
        
ОПИСАНИЕ

Проект для создания образовательных модулей и обучения

ТЕХНОЛОГИИ
* Python
* Django
* PostgreSQL
* Docker
* Docker-compose

Для работы с проектом:   
Склонируйте этот репозиторий к себе

В виртуальном окружении установите все зависимости:
pip install -r requirements.txt

Создайте файл .env по подобию .env.sample в корневой директории и заполните необходимые переменные окружения:

ADMIN_USER=имя администра для регистрации в админке
ADMIN_PASSWORD=пароль администратора

POSTGRES_DB=имя базы данных
POSTGRES_USER=пользователь базы данных 
POSTGRES_PASSWORD=пароль пользователя

Примените миграции:
python manage.py migrate

Запустите сервер:
python3 manage.py runserver

Используйте команду csu для создания тестового суперпользователя
python manage.py csu

Для работы в админке перейдите по адресу: http://127.0.0.1:8000/admin

Для запуска контейнеров через Docker: Запустите Docker, прожмите команду:
docker-compose up -d --build
