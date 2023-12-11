import xml.etree.ElementTree as et
import pandas as pd

price = []
description = []
calories = []
name = []

tree = et.parse('ADBMS/data.xml')
root = tree.getroot()

for food in root.iter('food'):
    name.append(food.find('name').text.strip())
    price.append(food.find('price').text.strip())
    description.append(food.find('description').text.strip())
    calories.append(food.find('calories').text.strip())

data = pd.DataFrame({'name':name, 'price': price, 'description': description, 'calories': calories})
print(data)

def query_xml(name, price, description, claories, data):
    if name:
        data = data[data['name'] == name] 
    if price:
        data = data[data['price'] == price] 
    if description:
        data = data[data['description'] == description] 
    if claories:
        data = data[data['claories'] == claories]
    
    return data
    
query_data = query_xml(
    name='Belgian Waffles',
    price='',
    description='',
    claories='',
    data=data
)
print(query_data)
