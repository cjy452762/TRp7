import requests


def ebox_list():
    #   c = '=‘ZjcwYjczYTktOTc1ZC00ZDg4LWFhYjYtODU5NTc2MzZjMThi’'
    r = requests.post('172.1.2.202:8001/metrics/msg-folws/ebox/list',
                      data={"keyword": "ebox",
                            "pageNum": 1,
                            "pageSize": 20
                            })
    print(r.json())


pass
