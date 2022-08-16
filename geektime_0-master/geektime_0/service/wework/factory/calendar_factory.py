from geektime_0.service.wework.api.calendar_http_api import CalendarHttpApi
from geektime_0.service.wework.api.portal_http_api import PortalHttpApi
from geektime_0.service.wework.api.session_http_api import SessionHttpApi
from geektime_0.service.wework.model.app import App
from geektime_0.service.wework.model.calendar import Calendar
from geektime_0.service.wework.model.calendar_api import CalendarApi
from geektime_0.service.wework.model.portal import Portal
from geektime_0.service.wework.model.session import Session
from geektime_0.service.wework.model.wework import WeWork


class CalendarFactory:
    @classmethod
    def create(cls, implement, session: Session, calendar: Calendar):
        if implement == 'service':
            return CalendarHttpApi(session)
        else:
            return CalendarApi(session)
