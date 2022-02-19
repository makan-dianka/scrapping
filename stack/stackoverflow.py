import requests
from bs4 import BeautifulSoup
import json 

url = "https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow"

res = requests.get(url)

cjson = res.json()
items_json = cjson["items"]

for element in items_json:
    print("Author : "+element['owner']['display_name'])
    print("Title  : "+element['title'])
    print("Tags   :",element['tags'])
  
    print("Link   : "+element['link'])
    print("Date   :",element['creation_date'])

    
    print("--" * 25)