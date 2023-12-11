import json
import pandas as pd

json_file = 'ADBMS/data.json'

with open(json_file) as file:
    json_data = json.load(file)

data = pd.DataFrame(json_data)
print(data)

def query_json(name, price, description, claories, data):
    if name:
        data = data[data['name'] == name] 
    if price:
        data = data[data['price'] == price] 
    if description:
        data = data[data['description'] == description] 
    if claories:
        data = data[data['claories'] == claories]
    
    return data
    
query_data = query_json(
    name='Belgian Waffles',
    price='',
    description='',
    claories='',
    data=data
)
print(query_data)