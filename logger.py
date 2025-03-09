import logging

# Настройка логирования
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Создание обработчика для записи логов в файл
handler = logging.FileHandler('celery_tasks.log')
handler.setLevel(logging.DEBUG)

# Форматирование логов
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(handler)
