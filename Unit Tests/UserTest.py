import django
django.setup()

import unittest
from datetime import datetime


# dt = datetime(year, month, day, hour, minute, second, microsecond)
# dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")


# TODO placeholder to get rid of errors
class User:
    def __init__(self, name='', email='', phone='0000000000', address='', courses=[], officeHours=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.courses = courses
        self.officeHours = officeHours




# MyUser : name, pw, Role
# name, email, phone, address, courses, office hours should all have default values
class TestUserGetName(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.user = User()
        self.user2 = User(name='John Doe', email='wildmudkip@gmail.com', phone='4141112222',
                                 address='South street', courses=self.course_list,
                                 officeHours=self.dt)

    def test_default_user_email(self):
        self.assertEqual(self.user.getName(), '')

    def test_default_user_email(self):
        self.assertEqual(self.user2.getName(), 'John Doe')


class TestUsersetName(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.user = User()
        self.user2 = User(name='John Doe', email='wildmudkip@gmail.com', phone='4141112222',
                                 address='South street', courses=self.course_list,
                                 officeHours=self.dt)

    def test_default_user_setName(self):
        self.user.setName("Peter Smith")
        self.assertEqual(self.user.getName(), 'Peter Smith')

    def test_default_user2_setName(self):
        self.user.setName("Jake Ewald")
        self.assertEqual(self.user2.getName(), 'Jake Ewald')


class TestUserGetEmail(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.user = User()
        self.user2 = User(name='John Doe', email='wildmudkip@gmail.com', phone='4141112222',
                                 address='South street', courses=self.course_list,
                                 officeHours=self.dt)

    def test_default_user_email(self):
        self.assertEqual(self.user.getEmail(), '')

    def test_default_user_email(self):
        self.assertEqual(self.user2.getEmail(), 'wildmudkip@gmail.com')

class TestUsersetEmail(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.user = User()
        self.user2 = User(name='John Doe', email='wildmudkip@gmail.com', phone='4141112222',
                                 address='South street', courses=self.course_list,
                                 officeHours=self.dt)

    def test_default_user_setEmail(self):
        self.user.setEmail("wildmudkip@uwm.edu")
        self.assertEqual(self.user.getEmail(), 'wildmudkip@uwm.edu')

    def test_default_user2_setEmail(self):
        self.user.setName("wildmudkip@yahoo.edu")
        self.assertEqual(self.user2.getEmail(), 'wildmudkip@yahoo.edu')

class TestUserGetPhone(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.user = User()
        self.user2 = User(name='John Doe', email='wildmudkip@gmail.com', phone='4141112222',
                                 address='South street', courses=self.course_list,
                                 officeHours=self.dt)

    def test_default_user_email(self):
        self.assertEqual(self.user.getPhone(), '')

    def test_default_user_email(self):
        self.assertEqual(self.user2.getPhone(), '4141112222')


class TestUsersetPhone(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.user = User()
        self.user2 = User(name='John Doe', email='wildmudkip@gmail.com', phone='4141112222',
                                 address='South street', courses=self.course_list,
                                 officeHours=self.dt)

    def test_default_user_setEmail(self):
        self.user.setPhone("2621112222")
        self.assertEqual(self.user.getPhone(), '2621112222')

    def test_default_user2_setEmail(self):
        self.user.setPhone("2621112222")
        self.assertEqual(self.user2.getPhone(), '2621112222')

class TestUserGetContact(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.user = User()
        self.user2 = User(name='John Doe', email='wildmudkip@gmail.com', phone='4141112222',
                                 address='South street', courses=self.course_list,
                                 officeHours=self.dt)

    def test_default_user_email(self):
        self.assertEqual(self.user.getPhone(), '')

    def test_default_user_email(self):
        self.assertEqual(self.user2.getPhone(),'John Doe', 'wildmudkip@gmail.com', '4141112222',
                                 'South street', self.course_list,
                                 self.dt)


class TestUserGetOH(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.user = User()
        self.user2 = User(name='John Doe', email='wildmudkip@gmail.com', phone='4141112222',
                                 address='South street', courses=self.course_list,
                                 officeHours=self.dt)

    def test_default_user_email(self):
        self.assertEqual(self.user.getOfficeHours(), '')

    def test_default_user_email(self):
        self.assertEqual(self.user2.getOfficeHours(), '12:30 15/06/2021')

class TestUsersetOH(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.user = User()
        self.user2 = User(name='John Doe', email='wildmudkip@gmail.com', phone='4141112222',
                                 address='South street', courses=self.course_list,
                                 officeHours=self.dt)

    def test_default_user_setEmail(self):
        self.user.setOfficeHours("10:30 06/06/2021")
        self.assertEqual(self.user.getOfficeHours(), '10:30 06/06/2021')

    def test_default_user2_setEmail(self):
        self.user.setOfficeHours("10:30 06/06/2021")
        self.assertEqual(self.user2.getOfficeHours(), '10:30 06/06/2021')


class TestUserGetAddress(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.user = User()
        self.user2 = User(name='John Doe', email='wildmudkip@gmail.com', phone='4141112222',
                                 address='South street', courses=self.course_list,
                                 officeHours=self.dt)

    def test_default_user_email(self):
        self.assertEqual(self.user.getAddress(), '')

    def test_default_user_email(self):
        self.assertEqual(self.user2.getAddress(), 'South street')

class TestUsersetAddress(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.user = User()
        self.user2 = User(name='John Doe', email='wildmudkip@gmail.com', phone='4141112222',
                                 address='South street', courses=self.course_list,
                                 officeHours=self.dt)

    def test_default_user_setEmail(self):
        self.user.setAddress("Greenfield Ave")
        self.assertEqual(self.user.getAddress(), 'Greenfield Ave')

    def test_default_user2_setEmail(self):
        self.user.setAddress("Greenfield Ave")
        self.assertEqual(self.user2.getAddress(), 'Greenfield Ave')