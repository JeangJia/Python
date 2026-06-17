import requests

target_url = "https://www.tiobe.com/tiobe-index/"
# 发送请求,获取数据
response = requests.get(target_url)
print(response.text)