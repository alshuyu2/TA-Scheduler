from datetime import datetime
# import str
# import instructor
# import TA
# import labs
# from instructor import Instructor
# import TA_schedule.Lab
from .UserInterface import UserInterface


class TA(UserInterface):
    def __init__(self, name='', email='', phone='', address='', office_hours='', courses=None, labs=None):
        if labs is None:
            labs = []
        if courses is None:
            courses = []
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.labs = labs
        self.hours = office_hours
        self.courses = courses

    def setName(self, given_name):
        # if not isinstance(given_name, str):
        #     raise TypeError("Name must be of type str")

        self.name = given_name

    def getName(self):
        return self.name

    def set_email(self, given_email):
        # if not isinstance(given_email, str):
        #     raise TypeError("Email must be of type str")

        self.email = given_email

    def getEmail(self):
        return self.email

    def setPhone(self, given_phone):
        # if not isinstance(given_phone, str):
        #     raise TypeError("Phone must be of type str")

        self.phone = given_phone

    def getPhone(self):
        return self.phone

    def setAddress(self, given_address):
        # if not isinstance(self, given_address):
        #     raise TypeError("Address must be of type str")
        self.address = given_address

    def getAddress(self):
        return self.address

    def get_labs(self):
        return self.labs

    def set_hours(self, given_hours):
        # if not isinstance(given_hours, datetime):
        #     raise TypeError("Argument is not of type datetime")

        self.hours = given_hours

    def get_hours(self):
        return self.hours

    def getContactInfo(self):
        self.getEmail() + "," + self.getPhone() + "," + self.get_hours()

    def add_lab(self, given_lab):
        # if not isinstance(given_lab, Lab.Lab):
        #     raise TypeError("Lab must be of type lab")
        self.labs.append(given_lab)

    # def remove_lab(self, given_lab):
    #     # if not isinstance(given_lab, Lab):
    #     #     raise TypeError("Lab must be of type lab")
    #     self.labs.remove(given_lab)

    # def get_course(self):
    #     return self

    def get_courses(self):
        return self.courses

    def getOfficeHour(self):
        pass

    def setContactInfo(self, other):
        pass

    def setOfficeHour(self, other):
        pass

