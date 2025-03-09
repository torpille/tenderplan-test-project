import settings
from tasks import logger, GetPrintFormLinks

if __name__ == "__main__":
    initial_page_links = \
        [settings.BASE_LINK + str(i + 1) for i in range(settings.PAGES_COUNT)]
    async_result = GetPrintFormLinks().delay(initial_page_links)
    try:
        result = async_result.get(timeout=10)
        logger.info(result)
    except Exception as e:
        logger.info(f"Ошибка получения результата задачи: {e}")

