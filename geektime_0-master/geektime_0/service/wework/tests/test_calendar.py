import pytest

from geektime_0.service.petclinic.utils.log import log
from geektime_0.service.wework.factory.SessionFactory import SessionFactory
from geektime_0.service.wework.factory.portal_factory import PortalFactory
from geektime_0.service.wework.model.app import App
from geektime_0.service.wework.model.calendar import Calendar
from geektime_0.service.wework.model.calendar_api import CalendarApi
from geektime_0.service.wework.model.session import Session
from geektime_0.service.wework.model.wework import WeWork


class TestCalendar:
    def setup_class(self):
        implement = 'service'
        wework = WeWork()
        calendar_app = App()

        # session = Session(wework, calendar_app)
        session: Session = SessionFactory.create_session(implement, wework, calendar_app)

        self.portal_api = PortalFactory.create(implement, session)

    @pytest.mark.parametrize("calendar_data", [
        {'summary': 'demo', 'color': '#000000', 'organizer': 'sihan'}
    ])
    def test_add(self, calendar_data):
        log.debug(calendar_data)
        calendar = Calendar(**calendar_data)
        log.debug(calendar)
        # calendar.summary = "demo"
        # calendar.color = 'red'

        r = self.portal_api.add_calendar(calendar)
        assert r.json()['errcode'] == 0

        calendar_id = r.json()['cal_id']
        log.debug(f'id = {calendar_id}')

        calendar_list = self.portal_api.list(calendar_id)
        log.debug(calendar_list)
        assert calendar in calendar_list
    #
    # def test_del(self):
    #     calendar_list = self.calendar_api.list()
    #     calendar_demo = calendar_list[0]
    #     calendar_demo.delete()
    #
    #     calendar_list = self.calendar_api.list()
    #     assert calendar_demo not in calendar_list

    def test_unique(self):
        ...
