from time import sleep

from mypy.dmypy_util import receive

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.reading_files import read_transactions_csv, read_transactions_excel
from src.widget import get_date, mask_account, mask_account_card
from src.utils import load_operations
#
# card_number = get_mask_card_number("1234567890123456")
# print(card_number)
#
# account_number = get_mask_account("12345678901234566598")
# print(account_number)
#
# shifr_card = mask_account_card("Maestro 1596837868705199")
# print(shifr_card)
#
# shifr_account = mask_account("Счет 64686473678894777654")
# print(shifr_account)
#
# data_string = get_date("2024-03-11T02:26:18.671407")
# print(data_string)
#
# filler_state = filter_by_state(
#     [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ],
#     state="CANCELED",
# )
# print(filler_state)
#
# sort_data = sort_by_date(
#     [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
# )
#
#
# transactions = [
#     {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702",
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188",
#     },
# ]
#
# usd_transactions = filter_by_currency(transactions, "USD")
# for _ in range(2):
#     print(next(usd_transactions))
#
#
# descriptions = transaction_descriptions(transactions)
# for _ in range(2):
#     print(next(descriptions))
#
#
# for card_number in card_number_generator(1, 5):
#     print(card_number)
#
#
# if __name__ == "__main__":
#     csv_path = "data/transactions.csv"
#     excel_path = "data/transactions_excel.xlsx"
#
#     csv_data = read_transactions_csv(csv_path)
#     print(f"Прочитано из CSV: {len(csv_data)} записей")
#
#     excel_data = read_transactions_excel(excel_path)
#     print(f"Прочитано из Excel: {len(excel_data)} записей")


def main():
    print('Привет! Добро пожаловать в программу работы с банковскими транзакциями. ')
    sleep(2)
    print('Выберите необходимый пункт меню:')
    print('1. Получить информацию о транзакциях из JSON-файла')
    print('2. Получить информацию о транзакциях из CSV-файла')
    print('3. Получить информацию о транзакциях из XLSX-файла')
    print('')
    info_transactions = input('Действие: ')

    while info_transactions.lower() != '1' and info_transactions.lower() != '2' and info_transactions.lower() != '3':
        print(f'Действие "{info_transactions}" недоступно.')
        info_transactions = input(
            'Введите действие из списка: '
            '\n1. Получить информацию о транзакциях из JSON-файла'
            '\n2. Получить информацию о транзакциях из CSV-файла'
            '\n3. Получить информацию о транзакциях из XLSX-файла'
        )

    if info_transactions == '1':
        print('Для обработки выбран JSON-файл.')

    elif info_transactions == '2':
        print('Для обработки выбран CSV-файл.')

    elif info_transactions == '3':
        print('Для обработки выбран XLSX-файл.')


    sleep(2)
    print('Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
    state = input('Статус: ')

    while state.lower() != 'executed' and state.lower() != 'canceled' and state.lower() != 'pending':
        print(f'Статус операции "{state}" недоступен.')
        state = input('Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')

    if state.lower() == 'executed':
        print(f'Операции отфильтрованы по статусу "EXECUTED"')

    elif state.lower() == 'canceled':
        print(f'Операции отфильтрованы по статусу "CANCELED"')

    elif state.lower() == 'pending':
        print(f'Операции отфильтрованы по статусу "PENDING"')


    sort_data = input('Отсортировать операции по дате? Да/Нет ')
    print('Отсортировать по возрастанию или по убыванию?')
    sort_order = input('по возрастанию/по убыванию ')
    filter_rub = input(' Выводить только рублевые транзакции? Да/Нет ')
    keyword_filter = input('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    keyword = ''
    if keyword_filter == 'да':
        keyword = input('Введите слово для фильтрации: ')
        print(f'Слово для фильтрации: {keyword}')


    sleep(2)
    print('Программа: Распечатываю итоговый список транзакций...')
    sleep(4)

    transactions = []
    if info_transactions == '1':
        transactions = load_operations('data/operations.json')

    elif info_transactions == '2':
        transactions = read_transactions_csv('data/transactions.csv')


    elif info_transactions == '3':
        transactions = read_transactions_excel('data/transactions_excel.xlsx')

# Фильтр по статусу
    filtered_transactions = filter_by_state(transactions, state)

# Фильтр по валюте
    if filter_rub.lower() == 'да':
        filtered_transactions = [
            trans for trans in filtered_transactions
            if 'rub' in str(trans.get('operationAmount', {}).get('currency', {}).get('code', '')).lower()
            or 'руб' in str(trans.get('operationAmount', {}).get('currency', {}).get('name', '')).lower()
            or 'rub' in str(trans.get('currency_code', '')).lower()
            or 'руб' in str(trans.get('currency_name', '')).lower()
        ]


# Фильтр по ключевому слову
    if keyword:
        keyword_transactions = []
        for trans in filtered_transactions:
            description = str(trans.get('description', '')).lower()
            if keyword.lower() in description:
                keyword_transactions.append(trans)
        filtered_transactions = keyword_transactions

# Фильтр по дате
    if sort_data == 'да':
        reverse_flag = (sort_order == 'по убыванию')
        filtered_transactions = sort_by_date(filtered_transactions, reverse=reverse_flag)

    if not filtered_transactions:
        print('Не найдено ни одной транзакции по вашему запросу')
    else:
        print(f'Всего банковских операций в выборке: {len(filtered_transactions)}')

# Вывод операций
    for trans in filtered_transactions:
        raw_date = trans.get('date', '')
        date_str = get_date(raw_date)

        description = trans.get('description')
        print(f'{date_str} {description}')

        sender = str(trans.get('from', ''))
        receiver = str(trans.get('to', ''))
        if sender:
            if 'счет' in sender.lower():
                sender = mask_account(sender)
            else:
                sender = mask_account_card(sender)

        if receiver:
            if 'счет' in receiver.lower():
                receiver = mask_account(receiver)
            else:
                receiver = mask_account_card(receiver)

        if sender and receiver:
            print(f'{sender} -> {receiver}')
        elif receiver:
            print(f'{receiver}')

        if 'operationAmount' in trans:
            amount = trans['operationAmount'].get('amount', '')
            currency = trans['operationAmount'].get('currency', {}).get('name', '')
        else:
            amount = trans.get('amount', '')
            currency = trans.get('currency_name', trans.get('currency', ''))

        print(f"Сумма: {amount} {currency}\n")





main()



