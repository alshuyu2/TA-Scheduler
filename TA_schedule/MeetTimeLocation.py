from abc import ABC, abstractmethod


class MeetTimeLocation(ABC):

    @abstractmethod
    def get_time_loc(self):
        pass

    @abstractmethod
    def get_meet_time(self):
        pass

    @abstractmethod
    def set_meet_time(self, other):
        pass

    @abstractmethod
    def get_loc(self):
        pass

    @abstractmethod
    def set_loc(self, other):
        pass
