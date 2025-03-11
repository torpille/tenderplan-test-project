# Tender Dates

## Описание проекта
Tender Dates — это проект, предназначенный для сбора данных о дате и времени публикации тендеров с сайта [zakupki.gov](http://zakupki.gov).


##  Предварительные требования


Docker: Убедитесь, что Docker установлен и работает на вашей машине.

Docker Compose: Убедитесь, что Docker Compose установлен.

Redis: Убедитесь, что Redis установлен, если это не так, то его необходимо установить:

```bash
   sudo apt update
   sudo apt upgrade
   sudo apt install redis-server
   sudo systemctl restart redis.service
```

## Установка

Для установки проекта выполните следующие шаги:

1. Склонируйте репозиторий:
   
```bash
   git clone https://github.com/torpille/tenderplan-test-project
   cd tenderplan-test-project
```

## Сборка и запуск через Docker Compose
Используйте Docker Compose для сборки и запуска контейнера:

   
```bash
   docker-compose up --build
```

## Остановка микросервиса
Для остановки микросервиса выполните:

```bash
   docker compose down
```

## Контакты

Если у вас есть вопросы или вам нужна помощь, вы можете связаться со мной torpille113@gmail.com

## Лицензия
The Unlicense

