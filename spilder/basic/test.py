import requests

result = requests.request('get', 'http://www.baidu.com')
print(result.text)
