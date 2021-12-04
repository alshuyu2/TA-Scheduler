import django
django.setup()
from django.contrib.auth.models import User
from TA_schedule.models import Class, Lab, TAtoClass, ClassToLab, PersonalInfo
from TA_schedule.roles import Role
import unittest
from datetime import datetime


# dt = datetime(year, month, day, hour, minute, second, microsecond)
# dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")


# TODO placeholder to get rid of errors
class Instructor:
    def __init__(self, name='', email='', phone='0000000000', address='', courses=[], officeHours=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.courses = courses
        self.officeHours = officeHours



class Courses:
    def __init__(self, name='', instr=''):
        self.instr = instr
        self.name = name


# MyUser : name, pw, Role
# name, email, phone, address, courses, office hours should all have default values
class TestInit(unittest.TestCase):
    def setUp(self):
        self.dt = datetime.strptime("12:30 15/06/2021", "%H:%M %d/%m/%Y")
        self.instr = Instructor()
        self.course_list = [Courses(instr=self.instr.name), Courses(instr=self.instr.name)]
        self.instr2 = Instructor(name='John Doe', email='wildmudkip@gmail.com', phone='4141112222',
                                 address='South street', courses=self.course_list,
                                 officeHours=self.dt)

    def test_default_instr_name(self):
        self.assertEqual(self.instr.name, '')

    # def test_default_instr_pw(self):
    #     self.assertEqual(self.instr.password, '')

    def test_default_instr_email(self):
        self.assertEqual(self.instr.email, '')

    def test_default_instr_phone(self):
        self.assertEqual(self.instr.phone, '0000000000')

    def test_default_instr_addr(self):
        self.assertEqual(self.instr.address, '')

    def test_default_instr_courses(self):
        self.assertListEqual(self.instr.courses, [])

    def test_default_instr_oh(self):
        self.assertEqual(self.instr.officeHours, None)

    def test_instr_name(self):
        self.assertEqual(self.instr2.name, 'John Doe')

    def test_instr_email(self):
        self.assertEqual(self.instr2.email, 'crazycookie@gmail.com')

    def test_instr_phone(self):
        self.assertEqual(self.instr2.phone, str(4141112222))

    def test_instr_addr(self):
        self.assertEqual(self.instr2.address, 'South street')

    def test_instr_courses(self):
        self.assertListEqual(self.instr2.courses, self.course_list)

    def test_instr_oh(self):
        self.assertEqual(self.instr2.officeHours, self.dt)


class TestGetCourses(unittest.TestCase):

    def setUp(self):
        self.course_list = [Courses('Bio'), Courses('English'), Courses('German')]
        self.instr = Instructor(name='John Johnathon')
        self.instr2 = Instructor(courses=self.course_list)
        self.user = User(first_name='John', last_name='Doe', email='wildmudkip@gmail.com').save()
        PersonalInfo(user_id=self.user, phone='4141112222', role=Role.INSTRUCTOR, address='South street').save()

    def test_get_course(self):
        self.assertEqual(self.instr2.courses, self.instr2.getCourses())

    def test_get_course_db(self):
        db_courses = list(PersonalInfo.objects.filter(user_id='John Johnathon').values())
        self.assertEqual(self.instr2.getCourses(), db_courses)


class TestAddCourse(unittest.TestCase):
    def setUp(self):
        self.course_list = self.course_list = [Courses('Bio'), Courses('English'), Courses('German')]
        self.instr = Instructor(name='Barry')
        Class(name='Bio', instr_id=User(username=self.instr.name)).save()
        # self.b = TAtoClass(Class(name='Bio'))
        # self.a = PersonalInfo(user_id=User(name='Barry', password='password', role=Role.INSTRUCTOR),
        #                          class_id=Classes(name='Bio 101', lab_id=Lab(name='903'))).save()

    def test_empty_course_add(self):
        self.instr.addCourse(Courses())
        self.assertEqual(1, len(list(Class.objects.filter(instr_id=self.instr.name))))

    def test_course_add(self):
        self.instr.addCourse(Courses(name='Bio'))
        self.assertListEqual(self.instr.courses, list(Class.objects.filter(user_id=self.instr))
                             .values_list(class_id__name='Bio'))


class TestRemoveCourse(unittest.TestCase):

    def setUp(self):
        self.course_list = self.course_list = [Courses('Bio'), Courses('English'), Courses('German')]
        self.instr = Instructor(name='Greg', courses=self.course_list)
        for i in self.course_list:
            Class(name=i, instr_id=User(username=self.instr.name)).save()

    def test_remove_empty_course(self):
        self.instr2 = Instructor()
        with self.assertRaises(ValueError, msg='list empty'):
            self.instr2.removeCourse(Courses('Bio'))

    def test_remove_course_not_present(self):
        with self.assertRaises(ValueError, msg='not found in list'):
            self.instr.removeCourse(Courses('CS361'))

    def test_remove_valid(self):
        self.instr.removeCourse(Courses('Bio'))
        self.assertListEqual(self.course_list.remove(Courses('Bio')), self.instr.courses)

    def test_remove_valid_db(self):
        self.instr.removeCourse(Courses('Bio'))
        self.assertListEqual(self.instr.courses, list(Class.objects.filter(user_id=self.instr)))
