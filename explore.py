import requests
server_answer = requests.get("https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json")
payload = server_answer.json()
print(payload.keys())
#print(type(payload))

print(payload['securities']['columns'])
print()
print(len(payload['securities']['data']))
print()
print(payload['securities']['data'][0])
print()
print(payload['securities'].keys())
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