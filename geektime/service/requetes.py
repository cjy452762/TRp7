import requests

def test():
    print("start")
    x=requests.post('http://litemall.hogwarts.ceshiren.com/wx/auth/login',
                      data={"username": "13123456789","password": "123456"})
    print(x.json())

