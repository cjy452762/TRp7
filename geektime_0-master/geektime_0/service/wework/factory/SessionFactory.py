from geektime_0.service.wework.api.session_http_api import SessionHttpApi
from geektime_0.service.wework.model.app import App
from geektime_0.service.wework.model.session import Session
from geektime_0.service.wework.model.wework import WeWork


class SessionFactory:
    @classmethod
    def create_session(cls, implement, wework: WeWork, app: App):
        if implement=='service':
            return SessionHttpApi(wework, app)
        else:
            return Session(wework, app)