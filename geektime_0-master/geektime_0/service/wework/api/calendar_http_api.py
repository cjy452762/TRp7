from dataclasses import asdict

import requests

from geektime_0.service.petclinic.utils.log import log
from geektime_0.service.wework.model.calendar import Calendar
from geektime_0.service.wework.model.calendar_api import CalendarApi
from geektime_0.service.wework.model.schedule import Schedule
from geektime_0.service.wework.model.session import Session


class CalendarHttpApi(CalendarApi):

    def add_schedule(self, schedule: Schedule):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/oa/schedule/add',
            params={'access_token': self.session.get_token()},
            json={'schedule': asdict(schedule)}
        )
        return r

    @classmethod
    def add(cls, calendar: Calendar, session: Session):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/oa/calendar/add',
            params={'access_token': session.get_token()},
            json={'calendar': asdict(calendar)}
        )
        log.debug('add_calendar')
        log.debug(r.json())



