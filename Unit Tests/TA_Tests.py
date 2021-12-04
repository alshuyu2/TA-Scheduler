import django
import unittest
django.setup()
from TA_schedule.models import MyUser
from TA_schedule.roles import Role
from datetime import datetime


class TA:
    def __init__(self, ta_name='', email='', phone='', address='', hours=None, courses=[], labs=[]):
        self.ta_name = ta_name
        self.ta_email = email
        self.phone = phone
        self.labs = labs
        self.hours = hours

        #self.role = role
        #self.class_name = class_name
        #self.user_id = user_id
        #office hours???
        MyUser().save()


class TestInit(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.ta = TA()
        self.example_ta = TA('Adriana', 'morale74@uwm.edu', '1234567890', 'kenwood blvd', [901], self.dt)

    def test_default_ta_name(self):
        self.assertEqual(self.ta.ta_name, '', "Default TA name is not as expected")

    def test_default_ta_email(self):
        self.assertEqual(self.ta.ta_email, '', "Default TA email is not as expected")

    def test_default_ta_phone(self):
        self.assertEqual(self.ta.phone, '', "Default TA phone is not as expected")

    def test_default_ta_address(self):
        self.assertEqual(self.ta.address, '', "Default TA address is not as expected")

    def test_default_ta_labs(self):
        self.assertEqual(self.ta.labs, [], "Default TA labs are not as expected")

    def test_default_ta_hours(self):
        self.assertEqual(self.ta.hours, None, "Default TA labs are not as expected")

    #def test_default_ta_role(self):
       #self.assertEqual(self.ta.role, Role.TA, "Default TA role is not as expected")

   # def test_default_ta_class_name(self):
        #self.assertEqual(self.ta.class_name, '', "Default TA class name is not as expected")

    #def test_default_ta_user_id(self):
        #self.assertEqual(self.ta.user_id, '', "Default TA user id is not as expected")

    def test_given_ta_name(self):
        self.assertEqual(self.example_ta.ta_name, 'Adriana', "Given TA name is not as expected")

    def test_given_ta_email(self):
        self.assertEqual(self.example_ta.ta_email, 'morale74@uwm.edu', "Given TA email is not as expected")

    def test_given_ta_phone(self):
        self.assertEqual(self.example_ta.phone, '1234567890', "Given TA phone is not as expected")

    def test_given_ta_address(self):
        self.assertEqual(self.example_ta.address, 'kenwood blvd', "Given TA address is not as expected")

    def test_given_ta_labs(self):
        self.assertEqual(self.ta.labs, [901], "Given TA labs are not as expected")

    def test_default_ta_hours(self):
        self.assertEqual(self.ta.hours, self.dt, "Given TA labs are not as expected")

    #def test_given_ta_role(self):
       # self.assertEqual(self.example_ta.role, Role.TA, "Given TA role is not as expected")

    #def test_given_ta_class_name(self):
       # self.assertEqual(self.example_ta.class_name, 'CS 361', "Given TA class is not as expected")

    #def test_given_ta_user_id(self):
        #self.assertEqual(self.example_ta.user_id, '991330188', "Given TA user id is not as expected")


class TestGetters(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.ta = TA()
        self.example_ta = TA('Adriana', 'morale74@uwm.edu', '1234567890', 'kenwood blvd', [901], self.dt)

    def test_default_get_name(self):
        a = self.ta.getName()
        self.assertEqual(a, '', "Cannot call getName on a null field")

    def test_default_get_email(self):
        a = self.ta.getEmail()
        self.assertEqual(a, '', "Cannot call getEmail on a null field")

    def test_default_get_phone(self):
        a = self.ta.getPhone()
        self.assertEqual(a, '', "GetPhone is not working as expected")

    def test_default_get_address(self):
        a = self.ta.getAddress()
        self.assertEqual(a, '', "GetAddress is not working as expected")

    def test_default_get_labs(self):
        a = self.ta.getLabs()
        self.assertEqual(a, [], "GetLabs is not working as expected")

    def test_default_get_hours(self):
        a = self.ta.getHours()
        self.assertEqual(a, None, "GetHours is not working as expected")

    def test_default_get_contact(self):
        a = self.ta.getContactInfo()
        self.assertEqual(a, 'TA Contact Info:'+ self.ta.getEmail() + ' ' + self.ta.getPhone() + ' '+self.ta.getHours(),
                         "GetContactInfo is not working as expected")

    def test_given_get_name(self):
        a = self.example_ta.getName()
        self.assertEquals(a, 'Adriana', "GetName is not working as expected")

    def test_given_get_phone(self):
        a = self.example_ta.getPhone()
        self.assertEqual(a, '123456789', "GetPhone is not working as expected")

    def test_given_get_address(self):
        a = self.example_ta.getAddress()
        self.assertEqual(a, 'kenwood blvd', "GetAddress is not working as expected")

    def test_given_get_labs(self):
        a = self.example_ta.getLabs()
        self.assertEqual(a, [901], "getLabs is not working as expected")

    def test_given_get_hours(self):
        a = self.example_ta.getHours()
        self.assertEqual(a, self.dt, "GetLabs is not working as expected")

    def test_given_get_contact(self):
        a = self.example_ta.getContactInfo()
        self.assertEqual(a, 'TA Contact Info:'+ self.example_ta.getEmail() + ' ' + self.example_ta.getPhone() + ' ' +
                         self.example_ta.getHours(), "GetContactInfo is not working as expected")


class TestSetters(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.ta = TA()
        self.example_ta = TA('Adriana', 'morale74@uwm.edu', '1234567890', 'kenwood blvd', [901], self.dt)

    def test_default_set_name(self):
        self.ta.setName('Ben')
        a = self.ta.getName()
        self.assertEqual(a, 'Ben', "Set name is not working as expected")

    def test_given_set_name(self):
        self.example_ta.setName('Ben')
        a = self.example_ta.getName()
        self.assertEqual(a, 'Ben', "Set name is not working as expected")

    def test_default_set_email(self):
        self.ta.setEmail('morale74@uwm.edu')
        a = self.ta.getEmail()
        self.assertEqual(a, 'morale74@uwm.edu', "Set email is not working as expected")

    def test_given_set_email(self):
        self.example_ta.setEmail('noname@uwm.edu')
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
        self.ta.setHours(datetime.strptime("12:30 15/08/2021", "%H:%M %d/%m/%Y"))
        a = self.ta.getHours()
        self.assertEqual(a, datetime.strptime("12:30 15/08/2021", "%H:%M %d/%m/%Y"), "Set hours is not working as expected")

    def test_given_set_hours(self):
        self.example_ta.setHours(datetime.strptime("12:30 15/08/2021", "%H:%M %d/%m/%Y"))
        a = self.example_ta.getHours()
        self.assertEqual(a, datetime.strptime("12:30 15/08/2021", "%H:%M %d/%m/%Y"),
                         "Set hours is not working as expected")


class TestAddRemove(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.ta = TA()
        self.example_ta = TA('Adriana', 'morale74@uwm.edu', '1234567890', 'kenwood blvd', [901], self.dt)

    def test_default_add_lab(self):
        self.ta.addLab('903')
        self.assertEqual(self.ta.labs, [903], "addLab is not working as expected")

    def test_given_add_lab(self):
        self.example_ta.addLab('903')
        self.assertEqual(self.example_ta.labs, [901, 903], "addLab is not working as expected")

    def test_default_remove_lab(self):
        with AssertionError(ValueError):
            self.assertEqual(self.ta.removeLab('903'), "Can't call remove on an empty lab array")

    def test_given_remove_lab(self):
        self.example_ta.removeLab('901')
        a = self.example_ta.getLabs()
        self.assertEqual(a, [], "Remove lab is not working as expected")
