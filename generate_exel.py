import random
import faker
import csv
from datetime import datetime, timedelta

# Инициализация Faker для генерации случайных данных
fake = faker.Faker('ru_RU')


# Функция для генерации случайной даты
def generate_random_date(start_year=1950, end_year=2000):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + timedelta(days=random_days)


# Функция для генерации случайного номера СНИЛС
def generate_snils():
    snils = ''.join([str(random.randint(0, 9)) for _ in range(11)])
    return f"{snils[:3]}-{snils[3:6]}-{snils[6:9]} {snils[9:11]}"


# Создание и открытие CSV файла для записи
with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Заголовок
    writer.writerow(['Гражданство', 'Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Серия паспорта', 'Номер паспорта',
                     'Когда выдан','Код подразделения', 'Кем выдан', 'СНИЛС', 'Обьект'])

    # Генерация 2000 строк данных
    for _ in range(2001):
        citizenship = 'РОССИЯ'
        last_name = fake.last_name()
        first_name = fake.first_name()
        patronymic = fake.first_name()
        birth_date = generate_random_date()
        passport_series = f"{random.randint(1000, 9999)}"
        passport_number = f"{random.randint(100000, 999999)}"
        issue_date = fake.date_this_decade()
        code = '770-001'
        who_gift = "ОУФМС России по Тестам"
        snils = generate_snils()
        warehouse = 1020001188926000

        # Запись строки в файл
        writer.writerow(
            [citizenship, last_name, first_name, patronymic, birth_date.strftime('%d.%m.%Y'), passport_series,
             passport_number, issue_date, code, who_gift, snils, warehouse])

print("Файл 'data.csv' успешно создан!")
