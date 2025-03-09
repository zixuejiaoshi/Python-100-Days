import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/item/43266129.json'
r = requests.get(url)   # 获取响应状态码
print(type(r))  # <class 'requests.models.Response'>
print(r.text)   # 响应内容的字符串形式
print(r.content) # 响应内容的二进制形式
print(r.status_code)    # 响应状态码
print(r.encoding)    # 响应内容的编码方式

requests_dict = r.json()
readable_file = 'readable_hn_data.json'
with open(readable_file, 'w') as f: # 写入文件
    json.dump(requests_dict, f, indent=4)