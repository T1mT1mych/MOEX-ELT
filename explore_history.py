import requests

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

params = {
    'from': '2026-01-01',
    'till': '2026-09-30',
    'start': 100
}
server_answer = requests.get("https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/SBER.json", params=params, timeout=30)
payload = server_answer.json()

rows = block_to_list_of_dicts(payload['history'])

for name in payload:
    rows_of_current_block = block_to_list_of_dicts(payload[name])
    if len(rows_of_current_block) != 0:
        print(name, "--->", "строк:", len(rows_of_current_block))
    else:
        print(name, "--->", "В данных нет строк")

#print("Дата первой строки:", rows[0]['TRADEDATE'])
#print("Дата последней строки:", rows[-1]['TRADEDATE'])

for name in payload['history']['columns']:
    print(name)
print()
print(len(payload['history']['columns']))

for day in rows[:3]:
    print(day['TRADEDATE'], day['OPEN'], day['LOW'], day['HIGH'], day['CLOSE'], day['VOLUME'], day['VALUE'], day['NUMTRADES'])

#print(block_to_list_of_dicts(payload['history.cursor']))

#print(len(rows))
#print()
#print(server_answer.status_code, server_answer.reason, server_answer.url, sep='\n')