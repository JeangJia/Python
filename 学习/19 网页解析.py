# lxml 高性能的 HTML/XML 文档解析库 pip install lxml
from lxml import html
import requests

with open('demo_html.html', 'w', encoding='utf-8') as f:
    url = 'https://www.tiobe.com/tiobe-index/'
    doc = requests.get(url)
    f.write(doc.text)
    ret = html.fromstring(doc.text)
    top20_list = ret.xpath('//table[@id="top20"]/tbody/tr')
    for tr in top20_list:
        rank = tr.xpath('./td/text()')
        print(rank)
