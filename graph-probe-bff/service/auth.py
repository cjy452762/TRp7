from http import cookies

import requests

url = 'http://120.26.46.142:8002/api/auth/signin'
username = 'cjy@126.com'
password = '123456'

session = requests.session()
data = {'username': username, 'password': password}
response=session.post(url=url,data=data)


# 登录
def test_signin():
    r = requests.post('http://120.26.46.142:8002/api/auth/signin',
                      data={"username": "cjy@126.com", "password": "123456"},
                      cookies={'cookie1': 'cookie1 value'})
  #  print(r.cookies)

   # cookies = requests.utils.dict_from_cookiejar(r.cookies)
#    print(cookies)
    assert r.status_code == 200
    print(r.json())


# 注册
def test_signup():
    r = requests.post('http://120.26.46.142:8002/api/auth/signup',
                      data={"email": "gs@163.com",
                            "phone": "133123456769",
                            "nikename": "gs",
                            "birthday": "1994-05-09",
                            "qq": "1243423423",
                            "password": "123456",
                            "pwdconfirm": "123456"})
    print(r)
    print(r.json())
    pass


# 登出
def test_signout():
    r = requests.get('http://120.26.46.142:8002/api/auth/signout')
    print(r.json())
    pass


# 用户查询
def test_user_list():
    url = 'http://120.26.46.142:8002/api/auth/signin'
    username = 'cjy@126.com'
    password = '123456'

    session = requests.session()
    data = {'username': username, 'password': password}
    response = session.post(url=url, data=data)
    print(response.json())

    index_url = 'http://120.26.46.142:8002/api/users'
    index_page = session.post(url=index_url).text
    print(index_page)