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


def test_work1():
    x = Work1()
    x.dologin(userinfo)
    # print("登录用户=>", userinfo)
    # 首个商品
    goods = x.doList()
    # print("首个商品=>", goods)
    # 获取首个商品详情
    productId = x.doDetail(goods)
    print("首个商品详情=>", productId)


class Work1:
    # 登录接口
    def dologin(self, userinfo):
        # 拼接登录url
        requestUrl = baseurl + '/wx/auth/login'
        body = json.dumps({"username": username,
                           "password": password
                           })
        response = requests.post(requestUrl, data=body, headers=headers)
        # print(response.text)
        # 登录成功
        assert response.status_code == 200
        res = json.loads(response.text)
        # print(type(res))
        # print( res['errmsg'])
        userinfo = res['data']
        headers['X-Litemall-Token'] = userinfo['token']
        # print('headers=>', headers)

    # 商品搜索接口
    def doList(self):
        requestUrl = baseurl + '/wx/goods/list'
        body = json.dumps({"keyword": "3d",
                           "page": 1,
                           "limit": 10
                           })
        response = requests.get(requestUrl, data=body, headers=headers)
        assert response.status_code == 200
        res = json.loads(response.text)
        print(res)
        goods = res['data']['list'][0]
        return goods;

    # 添加购物车接口
    def doDetail(self, goodsInfo):
        # print('goods detail=>', goodsInfo)
        requestUrl = "%s/wx/goods/detail?id=%d" % (baseurl, goodsInfo['id'])
        response = requests.get(requestUrl, data='', headers=headers)
        assert response.status_code == 200
        res = json.loads(response.text)
        productId = res['data']['specificationList'][0]['valueList'][0]
        return productId
        print('productId=>', res['data']['specificationList'][0]['valueList'][0])
