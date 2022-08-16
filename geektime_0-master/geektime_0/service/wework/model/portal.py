from geektime_0.service.wework.model.calendar import Calendar
from geektime_0.service.wework.model.calendar_api import CalendarApi
from geektime_0.service.wework.model.session import Session


class Portal:
    def __init__(self, session: Session):
        self.session = session

    def add_calendar(self, calendar: Calendar):
        calendar_api = CalendarApi.add(calendar, self.session)

    def list(self, *calendar_id_list):
        ...

    def get(self, calendar_id):
        ...
