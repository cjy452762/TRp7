import pytest

from geektime_0.service.petclinic.utils.log import log
from geektime_0.service.wework.factory.SessionFactory import SessionFactory
from geektime_0.service.wework.factory.calendar_factory import CalendarFactory
from geektime_0.service.wework.factory.portal_factory import PortalFactory
from geektime_0.service.wework.model.app import App
from geektime_0.service.wework.model.calendar import Calendar
from geektime_0.service.wework.model.calendar_api import CalendarApi
from geektime_0.service.wework.model.schedule import Schedule
from geektime_0.service.wework.model.session import Session
from geektime_0.service.wework.model.wework import WeWork


class TestSchedule:
    def setup_class(self):
        implement = 'service'
        wework = WeWork()
        calendar_app = App()

        # session = Session(wework, calendar_app)
        session: Session = SessionFactory.create_session(implement, wework, calendar_app)

        self.portal_api = PortalFactory.create(implement, session)

        calendar_data_default = {'summary': 'demo', 'color': '#000000', 'organizer': 'sihan'}
        calendar = Calendar(**calendar_data_default)
        r = self.portal_api.add_calendar()
        calendar_id = r.json()['cal_id']
        # 链式调用
        # self.portal_api.get(calendar_id).add_schedule()
        #
        self.calendar_api = CalendarFactory.create(implement, session, calendar)

    @pytest.mark.parametrize("calendar_data", [
        {'summary': 'demo', 'color': '#000000', 'organizer': 'sihan'}
    ])
    def test_add(self, schedule_data):
        schedule = Schedule(**schedule_data)
        r = self.calendar_api.add_schedule(schedule)
        assert r
