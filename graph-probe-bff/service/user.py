import requests

url = 'http://120.26.46.142:8002/api/auth/signin'
username = 'cjy@126.com'
password = '123456'

session = requests.session()
data = {'username': username, 'password': password}
response = session.post(url=url, data=data)
print(response.json())

index_url = 'http://120.26.46.142:8002/api/users'
index_page = session.get(url=index_url).text
print(index_page)
