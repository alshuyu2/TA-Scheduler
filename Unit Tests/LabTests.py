import django
django.setup()
import unittest
from datetime import datetime
from TA_schedule.models import Class, Lab


# TODO only here to get rid of errors
class Lab:
    def __init__(self, course=None, meetTime=None, loc='', ta=None):
        self.course = course
        self.meetTime = meetTime
        self.loc = loc
        self.ta = ta


class TA:
    pass


class Courses:
    pass


class TestInit(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.lab = Lab()
        self.lab2 = Lab(Courses('Bio'), self.dt, 'EMS190', TA(name='John'))

    def test_default_course(self):
        self.assertIsNone(self.lab.course)

    def test_default_meetTime(self):
        self.assertIsNone(self.lab.meetTime)

    def test_default_loc(self):
        self.assertEqual(self.lab.loc, '')

    def test_default_ta(self):
        self.assertIsNone(self.lab.ta)

    def test_course(self):
        self.assertEqual(self.lab2.course, Courses('Bio'))

    def test_meetTime(self):
        self.assertEqual(self.lab2.meetTime, self.dt)

    def test_loc(self):
        self.assertEqual(self.lab2.loc, 'EMS190')

    def test_ta(self):
        self.assertEqual(self.lab2.ta, TA(name='John'))


class TestGetCourse(unittest.TestCase):
    def setUp(self):
        self.lab = Lab(Courses('Bio'), self.dt, 'EMS190', TA(name='John'))
        Classes(name='Bio', lab_id=self.lab).save()

    def test_get_course(self):
        self.assertEqual(self.lab.getCourse(), Courses('Bio'))

    def test_get_course_db(self):
        db_courses = list(LabEnrollment.objects.filter(lab_id=self.lab).values())
        self.assertEqual(self.instr2.getCourses(), db_courses.pop())


class TestGetTA(unittest.TestCase):
    def setUp(self):
        self.lab = Lab(Courses('Bio'), self.dt, 'EMS190', TA(name='John'))

    def test_getTA(self):
        self.assertEqual(self.lab.getTA(), TA(name='John'))


class TestSetTA(unittest.TestCase):
    def setUp(self):
        self.lab = Lab(Courses('Bio'), self.dt, 'EMS190')
        self.lab2 = Lab(Courses('Bio'), self.dt, 'EMS190', TA(name='John'))

    def test_setTA(self):
        self.lab.setTA(TA(name='John'))
        self.assertEqual(self.lab.ta, TA(name='John'))

    def test_setTA_already_set(self):
        self.lab2.setTA(TA(name='Roe'))
        self.assertEqual(self.lab2.ta, TA(name='Roe'))
