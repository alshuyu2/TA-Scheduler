from courses import Courses
import unittest
import courses
class MyTestCase(unittest.TestCase):
    # tas and labs are lists
    def test_good_Set_Loc(self):
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
          #a = getTime(User, Date)
          #b = getLocation(User, Date)


    def test_Good_getTimeAndLoc(self):
        with self.assertRaises(TypeError, msg="Time or Location is null"):
          #a = meeting(Null, Null)
