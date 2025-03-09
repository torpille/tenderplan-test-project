# Tender Dates

## Описание проекта
Tender Dates — это проект, предназначенный для сбора данных о дате и времени публикации тендеров. Он фокусируется на получении информации о датах публикации тендеров с сайта [zakupki.gov](http://zakupki.gov).

## Установка

Для установки проекта выполните следующие шаги:

1. Склонируйте репозиторий:
   
bash
   git clone https://github.com/torpille/tenderplan-test-project
   
   
2. Убедитесь, что у вас установлены следующие зависимости:
   - Redis
   - Python 3
   - Celery

## Использование

После установки выполните следующие команды для запуска проекта:

1. Активируйте виртуальное окружение:
   
bash
   source venv/bin/activate  # для Linux/Mac
   

2. Запустите Celery worker:
   
bash
   celery -A tasks worker --loglevel=info
   

3. Запустите основной файл проекта:
   
bash
   python main.py
   

## Контакты

Если у вас есть вопросы или вам нужна помощь, вы можете связаться со мной torpille113@gmail.com

## Лицензия
The Unlicense

