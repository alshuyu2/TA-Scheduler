# import django
# django.setup()
import unittest
from datetime import datetime
# from TA_schedule.models import Class, Lab
from TA_schedule.Lab import Lab
from TA_schedule.TA_Class import TA
from TA_schedule.course import Courses


class TestInit(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.lab = Lab()
        self.lab2 = Lab(course=Courses(loc='Bio'), meet_time=self.dt, loc='EMS190', ta=TA(name='John'))

    def test_default_course(self):
        self.assertIsNone(self.lab.course)

    def test_default_meetTime(self):
        self.assertIsNone(self.lab.meet_time)

    def test_default_loc(self):
        self.assertEqual(self.lab.loc, '')

    def test_default_ta(self):
        self.assertIsNone(self.lab.ta)

    def test_course(self):
        self.assertEqual(self.lab2.course.loc, Courses(loc='Bio').loc)

    def test_meetTime(self):
        self.assertEqual(self.lab2.meet_time, self.dt)

    def test_loc(self):
        self.assertEqual(self.lab2.loc, 'EMS190')

    def test_ta(self):
        self.assertEqual(self.lab2.ta.name, TA(name='John').name)


class TestGetCourse(unittest.TestCase):
    def setUp(self):
        self.lab = Lab(course=Courses(loc='Bio'))
        # Classes(name='Bio', lab_id=self.lab).save()

    def test_get_course(self):
        self.assertEqual(self.lab.get_course().loc, Courses(loc='Bio').loc)


class TestGetTA(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.lab = Lab(Courses('Bio'), self.dt, 'EMS190', TA(name='John'))

    def test_getTA(self):
        self.assertEqual(self.lab.get_ta().name, TA(name='John').name)


class TestSetTA(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.lab = Lab(Courses('Bio'), self.dt, 'EMS190')
        self.lab2 = Lab(Courses('Bio'), self.dt, 'EMS190', TA(name='John'))

    def test_setTA(self):
        test_ta = TA(name='John')
        self.lab.set_ta(test_ta)
        self.assertEqual(self.lab.ta.name, test_ta.name)

    def test_setTA_already_set(self):
        self.lab2.set_ta(TA(name='Roe'))
        self.assertEqual(self.lab2.ta.name, TA(name='Roe').name)
