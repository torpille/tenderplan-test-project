from typing import List

import requests
import xmltodict
from bs4 import BeautifulSoup
from celery import Task

import settings
from celery_app import app
from logger import logger
from utils import run_request


class GetPublishDate(Task):
    """
    Получение даты публикации печатной формы
    """
    name = 'get_publish_date'

    def run(self, link):
        verified_data = self.verify_response_data(link)
        if verified_data:
            publish_date = next(iter(verified_data.values())) \
                .get('http://zakupki.gov.ru/oos/EPtypes/1:commonInfo') \
                .get('http://zakupki.gov.ru/oos/EPtypes/1:publishDTInEIS')
            publish_data = f"Дата публикации страницы {link} - {publish_date}"
            logger.info(publish_data)
        return None

    def verify_response_data(self, link):
        """
        :param link: str, URL для запроса
        :return: dict, данные xml страницы печатной формы
        """
        response = run_request(
            link,
            headers=settings.HEADERS,
            retries=settings.RETRY_COUNT
        )
        xml_data = response.text
        if not xml_data.startswith('<?xml'):
            logger.warning(f'Отсутствуют данные по ссылке {link}')
            return None
        parsed_xml_data = xmltodict.parse(
            xml_data,
            process_namespaces=True
        )
        if len(parsed_xml_data) == 1:
            return parsed_xml_data


app.register_task(GetPublishDate())


class GetPrintFormLinks(Task):
    """
    Получение ссылок на печатные формы.
    """
    name = 'get_print_form_links'

    def run(self, links):
        initial_print_urls = self.extract_initial_print_urls(links)
        for print_form_link in self.convert_to_print_form_links(initial_print_urls):
            GetPublishDate().delay(print_form_link)

    def extract_initial_print_urls(self, links: List[str]) -> List[str]:
        """
        Извлечение ссылок на печатные формы из html-страниц.
        """
        initial_print_urls = []
        for link in links:
            try:
                response = run_request(link,
                                       headers=settings.HEADERS,
                                       retries=settings.RETRY_COUNT)
                soup = BeautifulSoup(response.text, 'html.parser')
                tenders = soup.find_all("div", class_="registry-entry__header-top__icon")
                for tender in tenders:
                    tender_info_links = tender.find_all('a')
                    urls = [t_inf['href'] for t_inf in tender_info_links if t_inf.has_attr('href')]
                    initial_print_urls.extend(self.filter_urls(urls))
            except requests.RequestException as e:
                logger.warning(f'Ошибка при получении ссылки {link}: {e}')
        return initial_print_urls

    def filter_urls(self, urls: List[str]) -> List[str]:
        return [url for url in urls if url.startswith(settings.PRINT_PREFIX)]

    def convert_to_print_form_links(self, initial_print_urls: List[str]) -> List[str]:
        return [
            settings.SITE_PREFIX + url.replace("view.", "viewXml.") for url in initial_print_urls
        ]


app.register_task(GetPrintFormLinks())


@app.task(bind=True)
def collect_links_from_page():
    """
    Формирование списка url страниц и запуск задачи получения данных
    """
    initial_page_links = [
        settings.BASE_LINK + str(i + 1) for i in range(settings.PAGES_COUNT)
    ]
    GetPrintFormLinks().delay(initial_page_links)
