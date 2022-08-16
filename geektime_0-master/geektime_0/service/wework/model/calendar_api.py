from dataclasses import dataclass

from geektime_0.service.wework.model.calendar import Calendar
from geektime_0.service.wework.model.schedule import Schedule
from geektime_0.service.wework.model.schedule_api import ScheduleApi
from geektime_0.service.wework.model.session import Session


@dataclass
class CalendarApi:

    def __init__(self, session: Session, calendar: Calendar = None):
        self.session = session
        self.calendar = calendar

    def set_session(self, session: Session):
        self.session = session

    @classmethod
    def add(cls, calendar: Calendar, session: Session):
        """
        从零到一，是类方法
        :param calendar:
        :return:
        """
        ...

    def update(self, calendar: Calendar):
        """
        在已有对象上操作，使用示例方法
        :param calendar:
        :return:
        """
        ...

    def delete(self):
        ...

    @classmethod
    def list(cls):
        ...

    def add_schedule(self, schedule: Schedule):
        ...
