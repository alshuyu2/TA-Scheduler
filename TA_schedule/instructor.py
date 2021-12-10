# import course
from datetime import datetime
# import TA_schedule.course
from .UserInterface import UserInterface


class Instructor(UserInterface):

    def __init__(self, name='', email='', phone='', address="", office_hours='', courses=None, labs=None):
        if courses is None:
            courses = []

        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.meetTime = office_hours
        self.courses = courses
        self.labs = labs

    def setName(self, name_add):
        self.name = name_add

    def getName(self):
        return self.name

    def setEmail(self, email_add):
        self.email = email_add

    def getEmail(self):
        return self.email

    def setPhone(self, phoneNum):
        self.phone = phoneNum

    def getPhone(self):
        return self.phone

    def setOfficeHour(self, officeHours):
        # if not isinstance(officeHours, datetime):
        #     raise TypeError("It's not of type time object")

        self.meetTime = officeHours

    def getOfficeHour(self):
        return self.meetTime

    def getContactInfo(self):
        return "Email:" + self.getEmail() + "\nPhone Number:" + self.getPhone() + "\nOffice Hours:" + self.getOfficeHours()

    def setAddress(self, addLoc):
        self.address = addLoc

    def getAddress(self):
        return self.address

    def addCourse(self, courseAdd):
        self.courses.append(courseAdd)

    def get_courses(self):
        return self.courses

    def get_labs(self):
        return self.labs

    def setContactInfo(self, other):
        pass

