from datetime import datetime
from .UserInterface import UserInterface


class Admin(UserInterface):

    def __init__(self, name=None, email=None, phone='', address="", office_hours=None, courses=None, labs=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.courses = courses
        self.labs = labs
        self.office_hours = office_hours

    def get_labs(self):
        return self.office_hours

    def getName(self):
        return self.name

    def setName(self, name_add):
        self.name = name_add

    def setEmail(self, email_add):
        self.email = email_add

    def getEmail(self):
        return self.email

    def setPhone(self, phoneNum):
        self.phone = phoneNum

    def getPhone(self):
        return self.phone

    def setAddress(self, addLoc):
        self.address = addLoc

    def getContactInfo(self):
        return "Email:" + self.getEmail() + "\nPhone number" + self.getPhone()

    def get_courses(self):
        return self.courses

    def getAddress(self):
        return self.address

    def setContactInfo(self, other):
        pass

    def setOfficeHour(self, other):
        pass

    def getOfficeHour(self):
        pass
