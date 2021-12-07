from django.test import TestCase, Client

from TA_schedule.forms import CourseCreateForm, LabCreateForm
from TA_schedule.models import User, Lab, Class, ClassToLab


class CourseFormTests(TestCase):
    def setUp(self) -> None:
        self.user = Client()
        self.info = {
            'username': 'Vince',
            'password': 'pw123'
        }
        self.u = User.objects.create_user(**self.info)
        self.c_info = {
            'name': 'Bio101',
            'instr_id': self.u,
        }
        self.l_info = {
            'section': 'lab 901',
            'ta_name': self.u
        }
        self.user.login(**self.info)

    def test_course_form(self):
        c_form = CourseCreateForm(data=self.c_info)
        self.assertTrue(c_form.is_valid())

    def test_course_form_dup(self):
        c_form = CourseCreateForm(data=self.c_info)
        for i in range(5):
            c_form.save()
        a = Class.objects.all().count()
        self.assertEqual(a, 1)


class LabFormTests(TestCase):
    def setUp(self) -> None:
        self.user = Client()
        self.info = {
            'username': 'Vince',
            'password': 'pw123'
        }
        self.u = User.objects.create_user(**self.info)
        # self.c_info = {
        #     'name': 'Bio101',
        #     'instr_id': self.u,
        # }
        self.l_info = {
            'section': 'lab 901',
            'ta_name': self.u
        }
        self.user.login(**self.info)

    def test_lab_form(self):
        l_form = LabCreateForm(data=self.l_info)
        # response = self.user.post('/addcourse/')
        # print(response.context['messages'])
        # print(response.request)
        # print(l_form.data)
        # print(l_form.instance)
        self.assertTrue(l_form.is_valid())

    def test_lab_form_dup(self):
        l_form = LabCreateForm(data=self.l_info)
        for i in range(5):
            l_form.save()
        a = Lab.objects.all().count()
        self.assertEqual(a, 1)


class CourseAdd(TestCase):
    def setUp(self) -> None:
        self.user = Client()

        self.info = {
            'username': 'Vincent',
            'password': 'pw123'
        }
        self.form_info = {
            'name': 'Bio101',
            'instr_id': '1',
            'section': 'lab 901',
            'ta_name': '1'
        }
        self.u = User.objects.create_user(**self.info)
        self.user.login(**self.info)

    def test_add_new_course_class(self):
        self.user.post('/addcourse/', self.form_info, follow=True)
        c_objects = list(Class.objects.all())
        self.assertEqual(len(c_objects), 1)

    def test_add_new_course_lab(self):
        self.user.post('/addcourse/', self.form_info, follow=True)
        l_objects = list(Lab.objects.all())
        self.assertEqual(len(l_objects), 1)

    def test_add_new_course_class_to_lab(self):
        self.user.post('/addcourse/', self.form_info, follow=True)
        ctl_objects = list(ClassToLab.objects.all())
        self.assertEqual(len(ctl_objects), 1)

    def test_add_redirect(self):
        response = self.user.post('/addcourse/', self.form_info, follow=True)
        self.assertEqual(response.request['PATH_INFO'], '/courses/')

    def test_add_dup_class(self):
        for i in range(5):
            self.user.post('/addcourse/', self.form_info, follow=True)
        c_objects = list(Class.objects.all())
        self.assertEqual(len(c_objects), 1)

    def test_add_dup_lab(self):
        for i in range(5):
            self.user.post('/addcourse/', self.form_info, follow=True)
        l_objects = list(Lab.objects.all())
        self.assertEqual(len(l_objects), 1)

    def test_add_dup_class_to_lab(self):
        for i in range(5):
            self.user.post('/addcourse/', self.form_info, follow=True)
        ctl_objects = list(ClassToLab.objects.all())
        self.assertEqual(len(ctl_objects), 1)

    def test_add_dup_redirect(self):
        self.user.post('/addcourse/', self.form_info, follow=True)
        response = self.user.post('/addcourse/', self.form_info, follow=True)
        self.assertEqual(response.request['PATH_INFO'], '/addcourse/')

    def test_add_multiple(self):
        self.user.post('/addcourse/', self.form_info, follow=True)
        self.user.post('/addcourse/', {'name':'a', 'instr_id': '1', 'section':'lab 22', 'ta_name': '1'}, follow=True)
        c_objects = list(Class.objects.all())
        l_objects = list(Lab.objects.all())
        ctl_objects = list(ClassToLab.objects.all())
        self.assertEqual(len(c_objects), 2)
        self.assertEqual(len(c_objects), len(l_objects), len(ctl_objects))

    def test_add_lots(self):
        for i in range(50):
            self.user.post('/addcourse/', self.form_info, follow=True)
            # change course name so it is not duplicate
            self.form_info['name'] = i
        c_objects = list(Class.objects.all())
        self.assertEqual(len(c_objects), 50)

    def test_add_lots_compare(self):
        for i in range(50):
            self.user.post('/addcourse/', self.form_info, follow=True)
            # change course name so it is not duplicate
            self.form_info['name'] = i
        c_objects = list(Class.objects.all())
        l_objects = list(Lab.objects.all())
        ctl_objects = list(ClassToLab.objects.all())
        self.assertEqual(len(c_objects), len(l_objects), len(ctl_objects))
