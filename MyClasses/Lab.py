from MeetTimeLocation import MeetTimeLocation


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
        self.meet_time = other
        return self.meet_time

    def get_loc(self):
        return self.loc

    def set_loc(self, other):
        self.loc = other
        return self.loc

    # non interface methods

    def get_course(self):
        return self.course

    def get_ta(self):
        return self.ta

    def set_ta(self, other):
        self.ta = other
        return self.ta
