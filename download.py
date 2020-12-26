import urllib.request
import json

def download():
    url = 'https://data.corona.go.jp/converted-json/covid19japan-all.json'
    title = 'COVID-19_data.json'
    urllib.request.urlretrieve(url, "{0}".format(title))
    with open('COVID-19_data.json',mode='r',encoding='utf-8') as f:
        jsn = json.load(f)
    
    with open('COVID-19_data.json',mode='w',encoding='utf-8') as f:
        clean_json = json.dumps(jsn, indent=4,ensure_ascii=False)
        f.write(clean_json)

download()