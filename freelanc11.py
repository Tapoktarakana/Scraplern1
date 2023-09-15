import requests
from bs4 import BeautifulSoup
import json

#------------------------- Этот блок для запроса к странице и её записи в файл-----------------------

#url = 'https://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
#
#headers = {
#  'Accept':'*/*',
#  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
#  }
#
#req = requests.get(url, headers=headers)
#src = req.text
##print(src)
#
#with open('index.html','w',encoding="utf-8") as file:
#  file.write(src)

#------------------------------------------------------

with open('index.html', encoding='utf-8') as file:
 src=file.read()

soup = BeautifulSoup(src, 'lxml')

all_product_href = soup.find_all(class_='mzr-tc-group-item-href')

all_cat_dict = {}

for i in all_product_href:
 te = i.text
 he = 'https://health-diet.ru' + i.get('href')
 
 all_cat_dict[te] = he

 with open('all_cat_dict.json','w', encoding='utf-8') as file:
  json.dump(all_cat_dict, file, indent=4, ensure_ascii=False)
