from geektime_0.service.wework.api.portal_http_api import PortalHttpApi
from geektime_0.service.wework.api.session_http_api import SessionHttpApi
from geektime_0.service.wework.model.app import App
from geektime_0.service.wework.model.portal import Portal
from geektime_0.service.wework.model.session import Session
from geektime_0.service.wework.model.wework import WeWork


class PortalFactory:
    @classmethod
    def create(cls, implement, session: Session):
        if implement == 'service':
            return PortalHttpApi(session)
        else:
            return Portal(session)
