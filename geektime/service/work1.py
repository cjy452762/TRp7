import requests
import json

baseurl = "https://litemall.hogwarts.ceshiren.com"
username = "qwe"
phone = "1312345679"
password = "123456"
headers = {
    "Content-Type": "application/json;charset=UTF-8"
}

userinfo={}

def test_work1init():
    x = Work1()
    x.dologin(userinfo)

class Work1:
    def dologin(self,userinfo):
        requestUrl = baseurl + '/wx/auth/login'
        print(requestUrl)
        body = json.dumps({"username": username,
                           "password": password
                           })
        response = requests.post(requestUrl,
                                 data=body, headers=headers)
        print(response.text)
        assert response.status_code == 200
        responseData = json.loads(response.text)
        print(type(responseData))
        userinfo = responseData['data']
        print('userinfo=>', userinfo)
