from datetime import datetime
import TA_schedule.instructor
import TA_schedule.TA_Class
import TA_schedule.Lab


# import instructor
# import TA
# import labs

# we can import stack overflow
class Courses:
    def __init__(self, instr=None, time=None, loc="", tas=[], labs=[]):
        self.instr = instr
        self.time = time
        self.loc = loc
        self.tas = tas
        self.labs = labs


    def getMeetTime(self):
        # if(self.time is None):
        #     raise ValueError
        #
        # gettime = "Meet time for the lab is" + str(self.time)
        # return gettime
        return self.time

    def setMeetTime(self, date):
        # try:
        #     checkNum = int(date)
        #
        # except ValueError:
        #     self.time = checkNum
        # else:
        #     print("The data parameter isn't an int")
        #     pass #It is not a number

        # check if date is a datetime object
        # if not isinstance(date, datetime):
        #     raise TypeError("Expected datetime but got something else instead")

        self.time = date

    def setLoc(self, location):
        self.loc = location

    def getLoc(self):
        return self.loc

    def setInstructor(self, settingInstructor):
        # if not isinstance(settingInstructor, instructor.Ins):
        #     raise TypeError("It is not of Instructor class")

        self.instr = settingInstructor

    def getInstr(self):
        return self.instr

    def addTAs(self, TA_add):
        # if not isinstance(TA_add, TA):
        #     raise TypeError("The parameter object isn't of type TA")

        self.tas.append(TA_add)

    def getTAs(self):
        return self.tas

    def addLabs(self, Lab_add):
        # if not isinstance(Lab_add, Lab):
        #     raise TypeError("The parameter object isn't of type labs")

        self.labs.append(Lab_add)

    def getLabs(self):
        return self.labs

    def getTimeAndLoc(self):
        return self.loc + ":" + self.time
