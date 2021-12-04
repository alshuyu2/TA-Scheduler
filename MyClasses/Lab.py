from MyClasses.MeetTimeLocation import MeetTimeLocation
from datetime import datetime


class Course:
    pass


class TA:
    pass


class Lab(MeetTimeLocation):

    def __init__(self, course=None, meet_time=None, loc='', ta=None):
        self.course = course
        self.meet_time = meet_time
        self.loc = loc
        self.ta = ta

    # interface methods

    def get_time_loc(self):
        return str(self.get_meet_time()) + ' ' + self.get_loc()

    def get_meet_time(self):
        return self.meet_time

    def set_meet_time(self, other):
        if not isinstance(other, datetime):
            raise TypeError('Must be datetime object')
        self.meet_time = other
        return self.meet_time

    def get_loc(self):
        return self.loc

    def set_loc(self, other):
        if not isinstance(other, str):
            raise TypeError('Must be str')
        self.loc = other
        return self.loc

    # non interface methods

    def set_course(self, course):
        if not isinstance(course, Course):
            raise TypeError('Must be course object')
        self.course = course

    def get_course(self):
        return self.course

    def get_ta(self):
        return self.ta

    def set_ta(self, other):
        if not isinstance(other, TA):
            raise TypeError('Must be TA object')
        self.ta = other
        return self.ta
