import requests

from geektime_0.service.petclinic.utils.log import log
from geektime_0.service.wework.model.app import App
from geektime_0.service.wework.model.session import Session
from geektime_0.service.wework.model.wework import WeWork


class SessionHttpApi(Session):
    def refresh_token(self, wework: WeWork, app: App):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={
                'corpid': wework.corpid,
                'corpsecret': app.secret
            }
        )
        log.debug(r.json())
        return r.json()['access_token']
