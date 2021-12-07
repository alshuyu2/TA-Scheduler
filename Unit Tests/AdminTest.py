# import django
# django.setup()

import unittest
from TA_schedule.admin_class import Admin


# dt = datetime(year, month, day, hour, minute, second, microsecond)
# dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")

#
# # TODO placeholder to get rid of errors
# class Admin:
#     def __init__(self, name='Admin', email='', phone='0000000000', address=''):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.address = address
#
#

# MyUser : name, pw, Role
# name, email, phone, address, courses, office hours should all have default values
class TestInit(unittest.TestCase):
    def setUp(self):
        self.admin = Admin()
        self.admin2 = Admin(name='John Doe', email='wildmudkip@gmail.com', phone='4141112222',
                                 address='South street')

    def test_default_admin_name(self):
        self.assertEqual(self.admin.name, None)

    def test_default_admin_email(self):
        self.assertEqual(self.admin.email, None)

    def test_default_admin_phone(self):
        self.assertEqual(self.admin.phone, '')

    def test_default_admin_addr(self):
        self.assertEqual(self.admin.address, '')


    def test_admin2_name(self):
        self.assertEqual(self.admin2.name, 'John Doe')

    def test_admin2_email(self):
        self.assertEqual(self.admin2.email, 'wildmudkip@gmail.com')

    def test_admin2_phone(self):
        self.assertEqual(self.admin2.phone, str(4141112222))

    def test_admin2_addr(self):
        self.assertEqual(self.admin2.address, 'South street')





