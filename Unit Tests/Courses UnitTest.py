import unittest
import django
from TA_schedule.course import Courses

from TA_schedule.Lab import Lab
from TA_schedule.TA_Class import TA





class TestInit(unittest.TestCase):
    def setUp(self):
        self.Course = Courses()

        self.Course1 = Courses('zac', "12:00" , 'library', ["mike", "paul"], ["CS 932"])

    def test_default_instr(self):
        self.assertIsNone(self.Course.instr)

    def test_default_time(self):
        self.assertIsNone(self.Course.time)

    def test_default_loc(self):
        self.assertEqual(self.Course.loc, '')

    def test_default_tas(self):

        self.assertEqual(self.Course.tas, [])

    def test_default_labs(self):
        self.assertEqual(self.Course.labs, [])


    def test_instr(self):
        self.assertEqual(self.Course1.instr, 'zac')

    def test_meetTime(self):

        self.assertEqual(self.Course1.time, "12:00")

    def test_loc(self):
        self.assertEqual(self.Course1.loc, 'library')

    def test_tas(self):
        self.assertEqual(self.Course1.tas, ["mike", "paul"])

    def test_labs(self):
        self.assertEqual(self.Course1.labs, ["CS 932"])


class Test_getTimeAndLoc(unittest.TestCase):
    def setUp(self):
        self.Course1 = Courses('zac', "12:00", 'library', ["mike", "paul"], ["CS 932"])

    def test_getTimeAndLoc(self):
        self.assertEqual(self.Course1.getTimeAndLoc(), "library:12:00")


class Test_addTas(unittest.TestCase):
    def setUp(self):
        self.ta = TA("cool guy")
        self.Course1 = Courses('zac', "12:00", 'library', [], ["CS 932"])

    def test_addTas(self):
        self.Course1.addTAs(self.ta)
        self.assertEqual(self.Course1.tas, [self.ta])

# class Test_removeTas(unittest.TestCase):
#     def setUp(self):
#         self.lab = Lab("CS 932")
#         self.Course1 = Courses('zac', "12:00", 'library', ["mike", "paul"], self.lab)
#
#     def test_removeTa(self):
#         self.Course1.removeLab(self.lab)
#         self.assertEqual(self.Course1.tas, [])

class Test_addLabs(unittest.TestCase):
    def setUp(self):
        self.Lab = Lab("CS 361")
        self.Course1 = Courses('zac', "12:00", 'library', ["mike", "paul"], [])

    def test_addLabs(self):
        self.Course1.addLabs(self.Lab)
        self.assertEqual(self.Course1.labs, [self.Lab])


# class Test_removeLab(unittest.TestCase):
#     def setUp(self):
#         self.Course1 = Courses('zac', "12:00", 'library', ["mike", "paul"], ["CS 932", "CS 212"])
#
#     def test_removeLab(self):
#         self.Lab = Lab("CS 932")
#         self.Course1.removeLab(self.Lab)
#         self.assertEqual(self.Course1.labs, ["CS 212"])
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
