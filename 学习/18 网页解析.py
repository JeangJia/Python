# lxml 高性能的 HTML/XML 文档解析库 pip install lxml
import requests
from lxml import html

with open('demo_html.html', 'r', encoding='utf-8') as f:
    html_text = f.read()
    # 解析 HTML 文本, 将其转换成文档对象
    document = html.fromstring(html_text)
    # 解析表头
    headers = document.xpath('//table/thead/tr/th/text()')
    print(headers)
    # 解析表内容
    content = document.xpath('//table/tbody/tr/td/text()')
    print(content)
