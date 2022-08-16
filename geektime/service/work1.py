import requests
import json

baseurl = "https://litemall.hogwarts.ceshiren.com"
username = "qwe"
phone = "1312345679"
password = "123456"
headers = {
    "Content-Type": "application/json;charset=UTF-8"
}
# 使用变量储存用户信息
userinfo = {}


def test_work1init():
    x = Work1()
    x.dologin(userinfo)
    x.test_doTest()


class Work1:
    def dologin(self, userinfo):
        # 拼接登录url
        requestUrl = baseurl + '/wx/auth/login'
        body = json.dumps({"username": username,
                           "password": password
                           })
        response = requests.post(requestUrl,
                                 data=body, headers=headers)
        # print(response.text)
        # 登录成功
        assert response.status_code == 200
        responseData = json.loads(response.text)
        # print(type(responseData))
        userinfo = responseData['data']
        headers['X-Litemall-Token'] = userinfo['token']
        # print('headers=>', headers)

    def test_doTest(self):
        requestUrl = baseurl + '/wx/goods/list'
        body = json.dumps({"keyword": "3D",
                           "page": 1,
                           "limit": 10
                           })
        response = requests.post(requestUrl,
                                 data=body, headers=headers)

        assert response.status_code == 200
        responseData = json.loads(response.text)
        print(responseData)
