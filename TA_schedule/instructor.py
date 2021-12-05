# import course
from datetime import datetime
import TA_schedule.course


# from UserInterface import UserInterface

class Instructor():
    def __init__(self, name=None, email=None, phone=None, address="", officehours=None, courses=[], labs=[]):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.meetTime = officehours
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

    def setOfficeHours(self, officeHours):
        if not isinstance(officeHours, datetime):
            raise TypeError("It's not of type time object")

        self.meetTime = officeHours

    def getOfficeHours(self):
        return self.meetTime

    def getContactInfo(self):
        return "Email:" + self.getEmail() + "\nPhone Number:" + self.getPhone() + "\nOffice Hours:" + self.getOfficeHours()

    def setAddress(self, addLoc):
        self.address = addLoc

    def getAddress(self):
        return self.address

    def addCourse(self, courseAdd):
        # if not isinstance(courseAdd, Courses):
        #     raise TypeError("The parameter is not of object course")
        # check if the course is already there

        if courseAdd in self.courses:
            raise Exception("The course is already assigned to the instructor")
            pass

        self.courses.append(courseAdd)

    def getMyCourses(self):
        return self.courses
