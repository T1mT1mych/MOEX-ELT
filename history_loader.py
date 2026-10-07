import requests
import time

def block_to_list_of_dicts(block):
    '''
    Преобразует блок данных в список словарей
    :param block: блок данных
    :return: список словарей
    '''
    rows = []
    for row in block['data']:
        rows.append(dict(zip(block['columns'], row)))
    return rows

def fetch_all_history_pages(ticker, date_start, end_date):
    '''
    Собирает порциями до отказа список словарей с тикером со всеми днями периода
    :param ticker: вызываемый тикер
    :param date_start: дата начала
    :param end_date: дата конца
    :return: возвращает список словарей, по словарю на каждый день
    '''
    start = 0
    all_rows = []
    history_url = 'https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/' + ticker + '.json'
    while True:
        server_answer = requests.get(history_url, params = {'from': date_start, 'till': end_date, 'start': start}, timeout = 30) 
        payload = server_answer.json()
        page_rows = block_to_list_of_dicts(payload['history'])
        if len(page_rows) == 0:
            break
        all_rows.extend(page_rows)
        print("Порядковый номер стартового элемента --->", start, "Текущая длина парса элементов --->", len(all_rows) , "Длина 1 порции --->", len(page_rows))
        start += 100
        time.sleep(0.5)
    return all_rows

check_sber = fetch_all_history_pages('SBER', '2026-01-01', '2026-09-30')
length_sber = len(check_sber)

print(check_sber[0]['TRADEDATE'], check_sber[-1]['TRADEDATE'])
print(length_sber)
