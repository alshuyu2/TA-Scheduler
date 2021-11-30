import unittest
from datetime import datetime
from TA_schedule.models import Class, Lab

class Courses:
    # tas and labs are lists
    def __init__(self, instr=None, time = None, loc = '', tas= None, labs = None):
        self.instr = instr
        self.meetTime = time
        self.loc = loc
        self.tas = tas
        self.labs = labs

    class TA:
        pass

    class Lab:
        pass

class TestInit(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("11:30 20/05/2021", "%H:%M %d/%m/%Y")
        self.Course = Courses()
        self.Course1 = Courses('zac', self.dt, 'library', {"mike", "paul"}, {"CS 932"})

    def test_default_instr(self):
        self.assertIsNone(self.Course.instr)

    def test_default_time(self):
        self.assertIsNone(self.Course.time)

    def test_default_loc(self):
        self.assertEqual(self.Course.loc, '')

    def test_default_tas(self):
        self.assertIsNone(self.Course.tas)

    def test_default_loc(self):
        self.assertIsNone(self.Course.labs)

    def test_instr(self):
        self.assertEqual(self.Course1.instr, 'zac')

    def test_meetTime(self):
        self.assertEqual(self.Course1.dt, self.dt)

    def test_loc(self):
        self.assertEqual(self.Course1.loc, 'library')

    def test_tas(self):
        self.assertEqual(self.Course1.tas, {"mike", "paul"})

    def test_labs(self):
        self.assertEqual(self.Course1.labs, {"CS 932"})


class Test_getTimeAndLoc(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("11:30 20/05/2021", "%H:%M %d/%m/%Y")
        self.Course1 = Courses('zac', self.dt, 'library', {"mike", "paul"}, {"CS 932"})

    def test_getTimeAndLoc(self):
        self.assertEqual(self.course1.getTimeAndLoc(), "11:30 library")


class Test_addTas(unittest.TestCase):
    def setUp(self):
        self.ta = "sam"
        self.Course1 = Courses('zac', self.dt, 'library', {"mike", "paul"}, {"CS 932"})

    def test_addTas(self):
        self.course1.addTAs(self.ta)
        self.assertEqual(self.Course1.tas, {"mike", "paul", "sam"})

class Test_removeTas(unittest.TestCase):
    def setUp(self):
        self.Course1 = Courses('zac', self.dt, 'library', {"mike", "paul"}, {"CS 932"})

    def test_removeTa(self):
        self.ta = "mike"
        self.course1.removeTA(self.ta)

        self.assertEqual(self.Course1.tas, {"paul"})

class Test_addLab(unittest.TestCase):
    def setUp(self):
        self.Lab = "CA 202"
        self.Course1 = Courses('zac', self.dt, 'library', {"mike", "paul"}, {"CS 932"})

    def test_addTas(self):
        self.course1.addLab(self.Lab)
        self.assertEqual(self.course1.labs, {"CS 932", "CA 202"})


class Test_removeLab(unittest.TestCase):
    def setUp(self):
        self.Course1 = Courses('zac', self.dt, 'library', {"mike", "paul"}, {"CS 932", "CS 212"})

    def test_removeLab(self):
        self.Lab = "CS 932"
        self.course1.removeLab(self.Lab)
        self.assertEqual(self.Course1.labs, {"CS 212"})
"""
test_good_Set_Loc(self):
        #Pre: para is a string
        #Post Location var is set to new input, NO SIDE EFFECT
        input = "Library"
        self.loc = input
        self.assertFalse(self.loc, input, msg="Input and Loc_Var are not equal")

    def test_bad_Set_Loc(self):
        #Pre: para is a string
        #Post Location var is set to new input, NO SIDE EFFECT
        with self.assertRaises(TypeError, msg="input is not a string "):
            self.loc = 123

    def test_get_good_Loc(self):
        #Precondition: loc instance variable is not null
        #Postcondition: returns a string of the location of the lab, NO SIDE EFFECT
        self.loc = "Library"
        GetLoc = self.loc
        self.assertEqual("Library", GetLoc, msg="The location from getLoc is not right")

    def test_get_bad_Loc(self):
        #Pre: parameter must be a string
        #post: loc variable is set to new input, NO SIDE EFFECT
        self.loc = 12312
        GetLoc = self.loc
        self.assertEqual("Library", GetLoc, msg="The location from getLoc is not right")

    def test_good_getMeetTime(self):
        #Precondition: meetTime instance variable is not null
        #Postcondition: returns a date of the meeting time of the lab, Side Effect
        self.time = "12:00"
        self.assertEqual("12:00", self.time, msg="The meet time does not match up ")

    def test_bad_getMeetTime(self):
        #Precondition: meetTime instance variable is not null
        #Postcondition: returns a date of the meeting time of the lab, Side Effect
        input = None
        self.time = input
        self.assertFalse("12:00", self.time, msg="The meet time does not match up ")

    def test_get_NULL_TimeAndLoc(self):
        with self.assertRaises(TypeError, msg="Time or Location is null"):
            input = None
          #a = getTime(User, Date)
          #b = getLocation(User, Date)

    def getInstr(self):
        return self.instr
        # if the instructor name is null, return false(?)

    def setInstr(self, instr):
        self.instr = instr
        #Check if it's false, if not, then do nothing since it returns a void method
        self.assertFalse(self.instr, instr, msg="The names are not the same")
"""
