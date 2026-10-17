import requests

#dict(zip(payload['securities']['columns'], payload['securities']['data'][0]))

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

server_answer = requests.get("https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json")
payload = server_answer.json()

rows = block_to_list_of_dicts(payload['securities'])
print(len(rows))

for name in payload:
    rows_of_current_block = block_to_list_of_dicts(payload[name])
    if len(rows_of_current_block) != 0:
        print(name, "--->", len(rows_of_current_block), "строк")
    else:
        print(name, "--->", "В данных нет строк")

for name in payload:
    rows_of_current_block = block_to_list_of_dicts(payload[name])
    if(name == 'securities'):
        for security in rows_of_current_block[:5]:
            print(name, "--->", security['SECID'], security['SHORTNAME'], security['PREVPRICE'])


"""
for name in payload:
    if len(payload[name]['data']) != 0:
        if any(column in payload[name]['columns'] for column in ('SECID', 'SHORTNAME', 'PREVPRICE')):
            for i in range(len(payload[name]['data'] < 5)):
                print(name, "--->", payload[name]['data'][i])
    else:
        print(f"{name} ---> В данных нет строк")
"""

"""
print()
for name in payload:
    if len(payload[name]['data']) != 0: 
        print(name, "--->", payload[name]['data'][0])
    else:
        print(name, "--->", "В данных нет строк")
print()
for name in payload:
    if len(payload[name]['data']) != 0: 
        print(dict(zip(payload[name]['columns'], payload[name]['data'][0])))
    else:
        print(name, "--->", "В данных нет строк")
"""