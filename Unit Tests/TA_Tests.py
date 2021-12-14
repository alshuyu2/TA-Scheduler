
# from TA_schedule.models import MyUser
from TA_schedule.TA_Class import TA
from datetime import datetime
import unittest


class TestInit(unittest.TestCase):
    def setUp(self):
        # self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.ta = TA()
        self.example_ta = TA('Adriana', 'morale74@uwm.edu', '1234567890', 'kenwood blvd',  "12", None, [901])

    def test_default_ta_name(self):
        self.assertEqual(self.ta.getName(), '', "Default TA name is not as expected")

    def test_default_ta_email(self):
        self.assertEqual(self.ta.email, '', "Default TA email is not as expected")

    def test_default_ta_phone(self):
        self.assertEqual(self.ta.phone, '', "Default TA phone is not as expected")

    def test_default_ta_address(self):
        self.assertEqual(self.ta.address, '', "Default TA address is not as expected")

    def test_default_ta_labs(self):
        self.assertEqual(self.ta.labs, [], "Default TA labs are not as expected")

    def test_default_ta_hours(self):
        self.assertEqual(self.ta.hours, '', "Default TA labs are not as expected")

    #def test_default_ta_role(self):
       #self.assertEqual(self.ta.role, Role.TA, "Default TA role is not as expected")

   # def test_default_ta_class_name(self):
        #self.assertEqual(self.ta.class_name, '', "Default TA class name is not as expected")

    #def test_default_ta_user_id(self):
        #self.assertEqual(self.ta.user_id, '', "Default TA user id is not as expected")

    def test_given_ta_name(self):
        self.assertEqual(self.example_ta.name, 'Adriana', "Given TA name is not as expected")

    def test_given_ta_email(self):
        self.assertEqual(self.example_ta.email, 'morale74@uwm.edu', "Given TA email is not as expected")

    def test_given_ta_phone(self):
        self.assertEqual(self.example_ta.phone, '1234567890', "Given TA phone is not as expected")

    def test_given_ta_address(self):
        self.assertEqual(self.example_ta.address, 'kenwood blvd', "Given TA address is not as expected")

    def test_given_ta_labs(self):
        self.assertEqual(self.example_ta.get_labs(), [901], "Given TA labs are not as expected")

    def test_default_ta_hours(self):
        self.assertEqual(self.ta.get_hours(), '', "Given TA labs are not as expected")

    #def test_given_ta_role(self):
       # self.assertEqual(self.example_ta.role, Role.TA, "Given TA role is not as expected")

    #def test_given_ta_class_name(self):
       # self.assertEqual(self.example_ta.class_name, 'CS 361', "Given TA class is not as expected")

    #def test_given_ta_user_id(self):
        #self.assertEqual(self.example_ta.user_id, '991330188', "Given TA user id is not as expected")


class TestGetters(unittest.TestCase):
    def setUp(self):
        self.ta = TA()
        self.example_ta = TA('Adriana', 'morale74@uwm.edu', '1234567890', 'kenwood blvd', "12", [901])

    def test_default_get_name(self):
        a = self.ta.getName()
        self.assertEqual(a, '', "Cannot call get_name on a null field")

    def test_default_get_email(self):
        a = self.ta.getEmail()
        self.assertEqual(a, '', "Cannot call get_email on a null field")

    def test_default_get_phone(self):
        a = self.ta.getPhone()
        self.assertEqual(a, '', "GetPhone is not working as expected")

    def test_default_get_address(self):
        a = self.ta.getAddress()
        self.assertEqual(a, '', "GetAddress is not working as expected")

    def test_default_get_labs(self):
        a = self.ta.get_labs()
        self.assertEqual(a, [], "GetLabs is not working as expected")

    # def test_default_get_hours(self):
    #     a = self.ta.get_hours()
    #     self.assertEqual(a, None, "GetHours is not working as expected")

    # def test_default_get_contact(self):
    #     a = self.ta.get_contact_info()
    #
    #     self.assertEqual(a, 'TA Contact Info:'+ self.ta.get_email() + ' ' + self.ta.get_phone() + ' '+self.ta.get_hours(),
    #                      "GetContactInfo is not working as expected")

    def test_given_get_name(self):
        a = self.example_ta.getName()
        self.assertEquals(a, 'Adriana', "GetName is not working as expected")

    def test_given_get_phone(self):
        a = self.example_ta.getPhone()
        self.assertEqual(a, '1234567890', "GetPhone is  working as expected")

    def test_given_get_address(self):
        a = self.example_ta.getAddress()
        self.assertEqual(a, 'kenwood blvd', "GetAddress is not working as expected")

    # def test_given_get_labs(self):
    #     a = self.example_ta.get_labs()
    #     self.assertEqual(a, [901], "get_labs is not working as expected")

    # def test_given_get_hours(self):
    #     a = self.example_ta.get_hours()
    #     self.assertEqual(a, self.dt, "GetLabs is not working as expected")

    # def test_given_get_contact(self):
    #     a = self.example_ta.get_contact_info()
    #     self.assertEqual(a, 'TA Contact Info:'+ self.example_ta.get_email() + ' ' + self.example_ta.get_phone() + ' ' +
    #                      self.example_ta.get_hours(), "GetContactInfo is not working as expected")


class TestSetters(unittest.TestCase):
    def setUp(self):
        self.ta = TA()
        self.example_ta = TA('Adriana', 'morale74@uwm.edu', '1234567890', 'kenwood blvd', "12", [901])

    def test_default_set_name(self):
        self.ta.setName('Ben')
        a = self.ta.getName()
        self.assertEqual(a, 'Ben', "Set name is not working as expected")

    def test_given_set_name(self):
        self.example_ta.setName('Ben')
        a = self.example_ta.getName()
        self.assertEqual(a, 'Ben', "Set name is not working as expected")

    def test_default_set_email(self):
        self.ta.set_email('morale74@uwm.edu')
        a = self.ta.getEmail()
        self.assertEqual(a, 'morale74@uwm.edu', "Set email is not working as expected")

    def test_given_set_email(self):
        self.example_ta.set_email('noname@uwm.edu')
        a = self.example_ta.getEmail()
        self.assertEqual(a, 'noname@uwm.edu', "Set email is not working as expected")

    def test_default_set_phone(self):
        self.ta.setPhone('1234567890')
        a = self.ta.getPhone()
        self.assertEqual(a, '1234567890', "Set phone is not working as expected")

    def test_given_set_phone(self):
        self.example_ta.setPhone('0987654321')
        a = self.example_ta.getPhone()
        self.assertEqual(a, '0987654321', "Set phone is not working as expected")

    def test_default_set_address(self):
        self.ta.setAddress('oakland ave')
        a = self.ta.getAddress()
        self.assertEqual(a, 'oakland ave', "Set address is not working as expected")

    def test_given_set_address(self):
        self.example_ta.setAddress('oakland ave')
        a = self.example_ta.getAddress()
        self.assertEqual(a, 'oakland ave', "Set address is not working as expected")

    def test_default_set_hours(self):
        self.ta.set_hours(datetime.strptime("12:30 15/08/2021", "%H:%M %d/%m/%Y"))
        a = self.ta.get_hours()
        self.assertEqual(a, datetime.strptime("12:30 15/08/2021", "%H:%M %d/%m/%Y"), "Set hours is not working as expected")

    def test_given_set_hours(self):
        self.example_ta.set_hours(datetime.strptime("12:30 15/08/2021", "%H:%M %d/%m/%Y"))
        a = self.example_ta.get_hours()
        self.assertEqual(a, datetime.strptime("12:30 15/08/2021", "%H:%M %d/%m/%Y"),
                         "Set hours is not working as expected")


# class TestAddRemove(unittest.TestCase):
#     def setUp(self):
#         self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
#         self.ta = TA()
#         self.example_ta = TA('Adriana', 'morale74@uwm.edu', '1234567890', 'kenwood blvd', [901], self.dt)
#
#     def test_default_add_lab(self):
#         self.ta.add_lab(903)
#         self.assertEqual(self.ta.labs, [903], "addLab is not working as expected")
#
#     def test_given_add_lab(self):
#         self.example_ta.add_lab(903)
#         self.assertEqual(self.example_ta.labs, [901, 903], "addLab is not working as expected")
#
#     def test_default_remove_lab(self):
#         self.ta.remove_lab(903)
#         with AssertionError(ValueError):
#             self.assertEqual(self.ta.remove_lab(903), "Can't call remove on an empty lab array")
#
#     def test_given_remove_lab(self):
#         self.example_ta.remove_lab(901)
#         a = self.example_ta.get_labs()
#         self.assertEqual(a, [], "Remove lab is not working as expected")
