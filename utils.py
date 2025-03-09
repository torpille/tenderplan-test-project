from time import sleep

import requests

from tasks import logger


def run_request(link, headers, retries=10):
    """
    Выполняет HTTP GET запрос с повтором в случае ошибки.

    :param link: str, URL для запроса
    :param headers: dict, заголовки для запроса
    :param retries: int, максимальное количество попыток
    :return: Response или None в случае неуспеха
    """
    status = None
    for attempt in range(retries):
        response = requests.get(link, headers=headers)
        status = response.status_code

        if status == 200:
            return response

        if status == 429:
            sleep(2 ** attempt)

            logger.warning(f'Получен статус 429. Повторная попытка из {retries}.')
            continue
        sleep(attempt)
        logger.warning(f'Получен статус {status}. Повторная попытка из {retries}.')
        continue

    logger.warning(f'{status} Недоступна ссылка {link}')
    return None
