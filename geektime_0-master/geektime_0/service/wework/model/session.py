from geektime_0.service.petclinic.utils.log import log
from geektime_0.service.wework.model.app import App
from geektime_0.service.wework.model.wework import WeWork


class Session:
    _access_token = None

    def __init__(self, wework: WeWork, app: App):
        self._access_token = self.refresh_token(wework, app)
        Session._access_token = self._access_token
        log.debug(f"token =  {self.get_token()}")

    def refresh_token(self, wework: WeWork, app: App):
        """
        获取token
        :param wework:
        :param app:
        :return:
        """
        ...

    def get_token(self):
        """
        字段的获取
        :return:
        """
        return self._access_token

    @classmethod
    def get_global_session(cls):
        return cls._access_token
