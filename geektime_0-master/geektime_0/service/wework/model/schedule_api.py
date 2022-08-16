from dataclasses import dataclass

from geektime_0.service.wework.model.schedule import Schedule


@dataclass
class ScheduleApi:

    @classmethod
    def add(cls, schedule: Schedule):
        ...

    def update(self, schedule: Schedule):
        ...

    def delete(self):
        ...

    def del_attendees(self):
        ...
