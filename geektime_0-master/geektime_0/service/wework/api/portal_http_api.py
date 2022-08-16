import json
from dataclasses import asdict

import requests

from geektime_0.service.petclinic.utils.log import log
from geektime_0.service.wework.api.calendar_http_api import CalendarHttpApi
from geektime_0.service.wework.model.calendar import Calendar
from geektime_0.service.wework.model.portal import Portal


class PortalHttpApi(Portal):
    def list(self, *calendar_id_list):
        # wcQKd-CgAAgDDL6syolIfnm3GEOKeMZw
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/oa/calendar/get',
            params={'access_token': self.session.get_token()},
            json={'cal_id_list': calendar_id_list}
        )

        log.debug(r.json())

        calendar_list = []
        for item in r.json()['calendar_list']:
            calendar = Calendar()
            calendar.summary = item['summary']
            calendar.color = item['color']
            calendar.organizer = item['organizer']
            calendar_list.append(calendar)

        return calendar_list

    def get(self, calendar_id):
        calendar = self.list(calendar_id)[0]
        return CalendarHttpApi(self.session, calendar)
