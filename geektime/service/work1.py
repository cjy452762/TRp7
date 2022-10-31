import pytest
import requests
import json

baseurl = "https://litemall.hogwarts.ceshiren.com"
username = "qwe"
phone = "1312345679"
password = "123456"
headers = {
    "Content-Type": "application/json;charset=UTF-8"
}


def test_work1():
    x = Work1()
    userinfo = x.dologin()
    # print("登录用户=>", userinfo)
    # 首个商品
    goods = x.doList()
    # print("首个商品=>", goods)
    # 获取首个商品详情
    pro = x.doDetail(goods)
    print("首个商品详rodu情=>", pro)
    # 获取购物车
    beforeCarts = x.doCart()
    # 添加购物车
    x.doadd(pro)
    # print("添加购物车成功")
    afterCarts = x.doCart()
    print('添加前商品数量：', beforeCarts['cartTotal']['goodsCount'])
    print('添加后商品数量：', afterCarts['cartTotal']['goodsCount'])
    assert afterCarts['cartTotal']['goodsCount'] > beforeCarts['cartTotal']['goodsCount']


class Work1:
    # 登录接口
    def dologin(self):
        # 拼接登录url
        requestUrl = baseurl + '/wx/auth/login'
        body = json.dumps({"username": username,
                           "password": password
                           })
        response = requests.post(requestUrl, data=body, headers=headers)
        assert response.status_code == 200
        res = json.loads(response.text)
        userinfo = res['data']
        headers['X-Litemall-Token'] = userinfo['token']
        return userinfo

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

    # 商品详情接口
    def doDetail(self, goodsInfo):
        requestUrl = "%s/wx/goods/detail?id=%d" % (baseurl, goodsInfo['id'])
        response = requests.get(requestUrl, data='', headers=headers)
        assert response.status_code == 200
        res = json.loads(response.text)
        productId = res['data']['specificationList'][0]['valueList'][0]
        # print('productId=>', res['data']['specificationList'][0]['valueList'][0])
        return productId

    # 添加购物车接口
    def doadd(self, pro):
        requestUrl = baseurl + '/wx/cart/add'
        body = json.dumps({
            "goodsId": pro['goodsId'],
            "number": 1,
            "productId": pro['id']
        })
        response = requests.post(requestUrl, data=body, headers=headers)
        res = json.loads(response.text)
        print('goodsIS=>', pro['id'])
        assert response.status_code == 200
        # assert res['error'] == 0

    def doCart(self):
        requesUrl = baseurl + '/wx/cart/index'
        response = requests.get(requesUrl, headers=headers)
        res = json.loads(response.text)
        return res['data']
