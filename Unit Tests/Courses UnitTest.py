import unittest


class MyTestCase(unittest.TestCase):
    def test_good_Set_Loc(self):
        #Pre: para is a string
        #Post Location var is set to new input, NO SIDE EFFECT
        #input = "Library"
        #Loc_Var = SetLoc(input)
        self.assertFalse(Loc_Var, input, msg="Input and Loc_Var are not equal")

    def test_bad_Set_Loc(self):
        #Pre: para is a string
        #Post Location var is set to new input, NO SIDE EFFECT
        with self.assertRaises(TypeError, msg="input is not a string "):
            #Loc_Var = SetLoc(123)

    def test_getLoc(self):
        #Precondition: loc instance variable is not null
        #Postcondition: returns a string of the location of the lab, NO SIDE EFFECT
        Loc_var = "Library"
        Loc = getLoc()
        self.assertEqual(Loc_var, Loc, msg="The location from getLoc is not right")


    def test_get_NULL_TimeAndLoc(self):
        with self.assertRaises(TypeError, msg="Time or Location is null"):
          #a = getTime(User, Date)
          #b = getLocation(User, Date)


    def test_Good_getTimeAndLoc(self):
        with self.assertRaises(TypeError, msg="Time or Location is null"):
          #a = meeting(Null, Null)
