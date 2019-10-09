import requests

url = 'http://httpbin.org/get'

response = requests.get(url)
response.encode = 'utf-8'
print(response.text)

# print("hello world!")
input()
