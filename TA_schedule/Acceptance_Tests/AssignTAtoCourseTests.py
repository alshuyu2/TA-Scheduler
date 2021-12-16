from django.test import TestCase, Client
from TA_schedule.models import User, PersonalInfo, Class, TAtoClass
from TA_schedule.forms import TAtoCourseAddForm
from TA_schedule.roles import Role


class TestForms(TestCase):
    def setUp(self) -> None:
        self.u_info = {
            'username': 'Vince',
            'password': 'pw123'
        }
        User.objects.create_user(**self.u_info)
        self.c_info = {
            'name': 'CS361',
            'instr_id': User.objects.all().first()
        }
        Class.objects.create(**self.c_info)
        self.p_info = PersonalInfo.objects.get(user__username=self.u_info['username'])
        self.p_info.role = Role.TA
        self.p_info.save()

    def test_valid_form(self):
        ta_form = TAtoCourseAddForm({'class_name': '1', 'ta_name': '1'})
        self.assertTrue(ta_form.is_valid())

    def test_invalid_empty_form(self):
        self.assertFalse(TAtoCourseAddForm().is_valid(), msg='emtpy invalid')

    def test_invalid_not_a_ta(self):
        self.p_info.role = Role.ADMIN
        self.p_info.save()
        self.assertFalse(TAtoCourseAddForm({'class_name': '1','ta_name': '1'}).is_valid())

    def test_invalid_one_arg(self):
        self.assertFalse(TAtoCourseAddForm({'class_name': '1'}).is_valid())

    def test_invalid_one_arg_other(self):
        self.assertFalse(TAtoCourseAddForm({'ta_name': '1'}).is_valid())


class Assigning(TestCase):
    def setUp(self) -> None:
        self.user = Client()
        self.u_info = {
            'username': 'Vince',
            'password': 'pw123'
        }
        User.objects.create_user(**self.u_info)
        self.user.login(**self.u_info)
        self.c_info = {
            'name': 'CS361',
            'instr_id': User.objects.all().first()
        }
        Class.objects.create(**self.c_info)
        self.p_info = PersonalInfo.objects.get(user__username=self.u_info['username'])
        self.p_info.role = Role.TA
        self.p_info.save()
        self.ttc = {
            'class_name': '1',
            'ta_name': '1'
        }

    def test_size_one(self):
        response = self.user.post('/addtatocourse/', self.ttc)
        print(response, response.request)
        self.assertEqual(1, TAtoClass.objects.count())

    def test_size_five(self):

        self.user.post('/addtatocourse/', self.ttc)
        # add 4 more tatoclass objects, have to have different users and classes
        # ugly but works
        for i in range(2, 6):
            self.ttc['class_name'], self.ttc['ta_name'] = str(i), str(i)
            self.u_info['username'] = i
            User.objects.create_user(**self.u_info)
            p = PersonalInfo.objects.get(user__username=self.u_info['username'])
            p.role = Role.TA
            p.save()
            self.c_info['name'] = str(i)
            Class.objects.create(**self.c_info)
            self.user.post('/addtatocourse/', self.ttc)

        self.assertEqual(5, TAtoClass.objects.count())

    def test_duplicate_ta_to_class(self):
        self.user.post('/addtatocourse/', self.ttc)
        size = TAtoClass.objects.count()
        for i in range(5):
            self.user.post('/addtatocourse/', self.ttc)
        size2 = TAtoClass.objects.count()
        self.assertEqual(size, size2)