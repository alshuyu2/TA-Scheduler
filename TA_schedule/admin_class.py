from datetime import datetime
import UserInterface


class Admin(UserInterface.UserInterface):

    def __init__(self, name=None, email=None, phone=None, address="", office_hour=None, courses=None, labs=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address


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
        return "Email:" + self.getEmail() + "\nPhone number"+ self.getPhone()


    def getAddress(self):
        return self.address

    def setContactInfo(self, other):
        pass

    def setOfficeHour(self, other):
        pass

    def getOfficeHour(self):
        pass
