import unittest
from TA_schedule import views
from django.test import TestCase, Client

from TA_schedule.forms import CourseCreateForm, LabCreateForm
from TA_schedule.models import User, Lab, Class, ClassToLab


# Create your tests here.
class AddLabToCourse(TestCase):
    def setUp(self) -> None:
        self.user = Client()
        self.info = {
            'username': 'Adriana',
            'password': 'adriana'
        }
        self.u = User.objects.create_user(**self.info)
        self.c_info = {
            'name': 'CS361',
            'instr_id': self.u,
        }
        self.l_info = {
            'section': 'lab 901',
            'ta_name': self.u
        }
        self.u = User.objects.create_user(**self.info)
        self.user.login(**self.info)

        #assign the TA to the course

    def test_valid_course(self):
        # check create course and create TA steal from other acceptance tests
        c_form = CourseCreateForm(data=self.c_info)
        self.assertTrue(c_form.is_valid())

    def test_add_new_lab(self):
        self.user.post('/addLabs/', self.form_info, follow=True)
        c_objects = list(ClassToLab.objects.all())
        self.assertEqual(len(c_objects), 1)
