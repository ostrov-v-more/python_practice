import requests
import csv
import json
from typing import Optional
import time
import logging
logger = logging.getLogger(__name__)

'''
Задача - получать список каждые 10 секунд и записывать в csv-файл с заголовками fact,length
json_list = [
    {
  "fact": "Fossil records from two million years ago show evidence of jaguars.",
  "length": 67
}
  ],
'''


def get_cat_fact() -> requests.Response:
    url = "https://catfact.ninja/fact"
    response = requests.get(url)
    logger.info(f'{response.status_code}')
    return response

def parse(response: requests.Response) -> Optional[list]:
    if response.status_code == 200:
        try:
            print([json.loads(response.text)])
            # return list(json.loads(response.text))
            return [json.loads(response.text)]
        except json.JSONDecodeError:
            logger.error("Ошибка парсинга")
            return None
        except Exception as e:
            logger.error(f"Неизвестная ошибка: {e}")
            return None
    return None

def save_fact_csv(data: list, path: str):
    with open(path, "a", encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        # writer.writerow(['fact', 'length'])
        for fact in data:
            writer.writerow([fact['fact'], fact['length']])

def schedule(path: str):
    while True:
        logger.info('Парсим')
        data = parse(get_cat_fact())
        if data:
            save_fact_csv(data, path)
            logger.info('Сохроняем')
        logger.info('Ждем 10 сек')
        time.sleep(10)


def test_1():
    schedule("cat_facts.csv")


