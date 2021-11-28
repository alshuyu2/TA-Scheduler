import django
import unittest
from TA_schedule.models import MyUser
#from TA_schedule.roles import Role
django.setup()


class TA:
    def __init__(self, ta_name='', phone='0000000000', role='TA', class_name='', user_id =''):
        self.ta_name = ta_name
        self.phone = phone
        self.role = role
        self.class_name = class_name
        self.user_id = user_id
        MyUser().save()


class TestInit(unittest.TestCase):
    def setUp(self):
        self.ta = TA()
        self.example_ta = TA('Adriana', '1234567890', 'TA', 'CS 361', '991330188')

    def test_default_ta_name(self):
        self.assertEqual(self.ta.ta_name, '', "Default TA name is not as expected")

    def test_default_ta_phone(self):
        self.assertEqual(self.ta.phone, '0000000000', "Default TA phone is not as expected")

    def test_default_ta_role(self):
        self.assertEqual(self.ta.role, 'TA', "Default TA role is not as expected" )

    def test_default_ta_class_name(self):
        self.assertEqual(self.ta.class_name, '', "Default TA class name is not as expected")

    def test_default_ta_user_id(self):
        self.assertEqual(self.ta.user_id, '', "Default TA user id is not as expected")

    def test_given_ta_name(self):
        self.assertEqual(self.example_ta.ta_name, 'Adriana', "Given TA name is not as expected")

    def test_given_ta_phone(self):
        self.assertEqual(self.example_ta.phone, '1234567890', "Given TA phone is not as expected")

    def test_given_ta_role(self):
        self.assertEqual(self.example_ta.role, 'TA', "Given TA role is not as expected")

    def test_given_ta_class_name(self):
        self.assertEqual(self.example_ta.class_name, 'CS 361', "Given TA class is not as expected")

    def test_given_ta_user_id(self):
        self.assertEqual(self.example_ta.user_id, '991330188', "Given TA user id is not as expected")

